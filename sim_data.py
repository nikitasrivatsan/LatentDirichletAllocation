#!/usr/bin/env python

# Generates simulated data for testing

from numpy import random

alpha = 0.5
beta = 0.5
K = 5
num_docs = 1000
len_doc = 500
vocab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

output = open("test", "w")
outphi = open("true-phi", "w")
outtheta = open("true-theta", "w")

# generate phi
phi = []
for i in range(0, K):
    x = random.dirichlet([beta] * len(vocab)).tolist()
    phi.append(x)
# print phi to file
for i in range(0, len(vocab)):
    outphi.write(vocab[i] + ' ')
    for topic in range(0, K):
        outphi.write(str(phi[topic][i]) + ' ')
    outphi.write('\n')

# generate data
for doc in range(0, num_docs):
    # generate theta
    theta = random.dirichlet([alpha] * K).tolist()
    for j in range(0, len_doc):
        # choose topic
        topic = 0
        point = random.uniform(0, 1)
        total = 0
        for i in range(0, K):
            total += theta[i]
            if total >= point:
                topic = i
                break
        # sample word
        word = ''
        point = random.uniform(0, 1)
        total = 0
        for i in range(0, len(vocab)):
            total += phi[topic][i]
            if total >= point:
                word = vocab[i]
                break
        output.write(word + ' ')
    output.write('\n')
    # write theta to file
    for weight in theta:
        outtheta.write(str(weight) + ' ')
    outtheta.write('\n')
