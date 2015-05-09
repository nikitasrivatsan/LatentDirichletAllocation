#!/usr/bin/env python

# Akshay Srivatsan
# asrivat1@jhu.edu

# Usage: ./analyze.py nameFile output

import sys

names = []
display = 15

class item:
    def __init__(self, name, theta):
        self.name = name
        self.theta = theta

def main():
    readName(sys.argv[1])
    (phi, K) = readPhi(sys.argv[2] + "-phi")
    theta = readTheta(sys.argv[2] + "-theta")

    # find the words most common in each topic
    print "Common Words in Topics"
    for k in range(0,K):
        freqwords = sorted(phi, key=lambda word: word.theta[k], reverse=True)
        print "Topic " + str(k) + ":"
        for x in freqwords[:display]:
            print x.name
        print ""

    # find the documents most aligned with each topic
    print "Documents with High Proportion of Topics"
    for k in range(0,K):
        freqdocs = sorted(theta, key=lambda word: word.theta[k], reverse=True)
        print "Topic " + str(k) + ":"
        for x in freqdocs[:display]:
            print x.name
        print ""


def readTheta(fileName):
    thetaFile = open(fileName)
    theta = []

    i = 0
    for line in thetaFile:
        line = line.strip()
        tokens = line.split()
        topics = [float(x) for x in tokens]
        theta.append(item(names[i], topics))
        i += 1

    return theta

def readPhi(fileName):
    phiFile = open(fileName)
    phi = []

    i = 0
    for line in phiFile:
        line = line.strip()
        tokens = line.split()
        word = tokens.pop(0)
        topics = [float(x) for x in tokens]
        K = len(topics)
        phi.append(item(word, topics))
        i += 1

    return (phi, K)

def readName(fileName):
    nameFile = open(fileName)

    for line in nameFile:
        line = line.strip()
        names.append(line)

    return names

if __name__ == "__main__":
    main()
