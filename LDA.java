import java.io.*;
import java.util.*;

public class LDA
{
    private static ArrayList<String[]> docs = new ArrayList<String[]>();
    private static ArrayList<int[]> z = new ArrayList<int[]>();
    private static HashMap<String, Integer> vocab = new HashMap<String, Integer>();
    private static int K = 0;
    private static int m = 0;
    private static int T = 0;
    private static int burnin = 0;
    private static double alpha = 0;
    private static double beta = 0;

    public static void main(String[] args)
    {
        String inputFileName = args[0];
        String outputFileName = args[1];
        K = Integer.parseInt(args[2]);
        alpha = Double.parseDouble(args[3]);
        beta = Double.parseDouble(args[4]);
        T = Integer.parseInt(args[5]);
        burnin = Integer.parseInt(args[6]);

        // set up io
        PrintWriter out_phi = null;
        PrintWriter out_theta = null;
        PrintWriter out_llik = null;
        try
        {
            out_phi = new PrintWriter(new File(outputFileName + "-phi"));
            out_theta = new PrintWriter(new File(outputFileName + "-theta"));
            out_llik = new PrintWriter(new File(outputFileName + "-llik"));
        }
        catch(FileNotFoundException e)
        {
            System.err.println("Error opening PrintWriter: " + e.getMessage());
        }

        // read in data
        readData(inputFileName);

        // initialize z
        Random rand = new Random();
        for(int i = 0; i < m; i++)
        {
            z.add(new int[docs.get(i).length]);
            for(int j = 0; j < z.get(i).length; j++)
            {
                z.get(i)[j] = rand.nextInt(K);
            }
        }

        // initialize counts
        int[][] n_d_k = new int[m][K];
        int[][] n_k_w = new int[K][vocab.size()];
        int[] n_k = new int[K];
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < docs.get(i).length; j++)
            {
                n_d_k[i][z.get(i)[j]]++;
                n_k_w[z.get(i)[j]][vocab.get(docs.get(i)[j])]++;
                n_k[z.get(i)[j]]++;
            }
        }

        // initialize parameters
        double[][] theta_d_k = new double[m][K];
        double[][] phi_k_w = new double[K][vocab.size()];
        double[][] theta_d_k_hat = new double[m][K];
        double[][] phi_k_w_hat = new double[K][vocab.size()];

        // perform iterations
        System.out.print("[                                                  ]");
        for(int t = 1; t <= T; t++)
        {
            // display progress
            for(int i = 0; i < 52; i++)
                System.console().printf("\u0008");
            String progress = "";
            progress += "[";
            for(int i = 0; i < T; i += T / 50)
            {
                if(i < t)
                {
                    progress += "=";
                }
                else
                {
                    progress += " ";
                }
            }
            progress += "]";
            System.console().printf(progress);

            // resample z
            for(int i = 0; i < m; i++)
            {
                for(int j = 0; j < z.get(i).length; j++)
                {
                    // remove z from counts
                    n_d_k[i][z.get(i)[j]]--;
                    n_k_w[z.get(i)[j]][vocab.get(docs.get(i)[j])]--;
                    n_k[z.get(i)[j]]--;
                    
                    // resample z
                    double[] weights = new double[K];
                    double weight_sum = 0;
                    for(int k = 0; k < K; k++)
                    {
                        weights[k] = ((n_d_k[i][k] + alpha) / (docs.get(i).length + K * alpha))
                        * ((n_k_w[k][vocab.get(docs.get(i)[j])] + beta) / (n_k[k] + vocab.size() * beta));
                        weight_sum += weights[k];
                    }
                    double point = Math.random() * weight_sum;
                    double cumulative = 0;
                    for(int k = 0; k < K; k++)
                    {
                        cumulative += weights[k];
                        if(cumulative >= point)
                        {
                            z.get(i)[j] = k;
                            break;
                        }
                    }
                    
                    // add z back to counts
                    n_d_k[i][z.get(i)[j]]++;
                    n_k_w[z.get(i)[j]][vocab.get(docs.get(i)[j])]++;
                    n_k[z.get(i)[j]]++;
                }
            }

            // estimate current parameters
            for(int i = 0; i < m; i++)
            {
                for(int k = 0; k < K; k++)
                {
                    theta_d_k[i][k] = (n_d_k[i][k] + alpha) / (docs.get(i).length + K * alpha);
                }
            }
            for(int k = 0; k < K; k++)
            {
                for(int w = 0; w < vocab.size(); w++)
                {
                    phi_k_w[k][w] = (n_k_w[k][w] + beta) / (n_k[k] + vocab.size() * beta);
                }
            }
            
            // update expected value of parameters
            if(t > burnin)
            {
                for(int i = 0; i < m; i++)
                {
                    for(int k = 0; k < K; k++)
                    {
                        theta_d_k_hat[i][k] *= t - 1 - burnin;
                        theta_d_k_hat[i][k] += (n_d_k[i][k] + alpha) / (docs.get(i).length + K * alpha);
                        theta_d_k_hat[i][k] /= t - burnin;
                    }
                }
                for(int k = 0; k < K; k++)
                {
                    for(int w = 0; w < vocab.size(); w++)
                    {
                        phi_k_w_hat[k][w] *= t - 1 - burnin;
                        phi_k_w_hat[k][w] = (n_k_w[k][w] + beta) / (n_k[k] + vocab.size() * beta);
                        phi_k_w_hat[k][w] /= t - burnin;
                    }
                }
            }

            // compute log likelihood
            double loglik = logLikelihood(theta_d_k, phi_k_w);
            out_llik.println(loglik);
        }
        System.out.println();

        // print out the parameters to file
        for(int i = 0; i < m; i++)
        {
            for(int k = 0; k < K; k++)
            {
                out_theta.print(theta_d_k_hat[i][k] + " ");
            }
            out_theta.println();
        }
        for(String word : vocab.keySet())
        {
            out_phi.print(word + " ");
            for(int k = 0; k < K; k++)
            {
                out_phi.print(phi_k_w_hat[k][vocab.get(word)] + " " );
            }
            out_phi.println();
        }

        out_phi.close();
        out_theta.close();
        out_llik.close();
    }

    private static double logLikelihood(double[][] theta_d_k, double[][] phi_k_w)
    {
        double loglik = 0;
        double innersum = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < docs.get(i).length; j++)
            {
                innersum = 0;
                for(int k = 0; k < K; k++)
                {
                    innersum += theta_d_k[i][k] * phi_k_w[k][vocab.get(docs.get(i)[j])];
                }
                loglik += Math.log(innersum);
            }
        }
        return loglik;
    }

    private static void readData(String fileName)
    {
        Scanner scan = null;
        try
        {
            scan = new Scanner(new File(fileName));
        }
        catch(FileNotFoundException e)
        {
            System.err.println("Input file not found: " + e.getMessage());
        }
        while(scan.hasNextLine())
        {
            String line = scan.nextLine().trim();
            docs.add(line.split(" "));
            for(String word : line.split(" "))
            {
                if(!vocab.containsKey(word))
                {
                    vocab.put(word, vocab.size());
                }
            }
            m++;
        }
    }
}
