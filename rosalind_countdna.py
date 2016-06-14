#Rosalind_countdna
#Objective: Count each nucleotide in a given sequence

'''DNA strand is composed of 4 different nucleotides A,C,G,T. This task will
perform how to count nucleotides in a sequence using python'''

import os
os.chdir('/home/vu/Downloads') #move to a desired directory
f = open('rosalind_dna (1).txt', 'r').read()[:-1] #[-1] for rm \n
d = {}
for i in f:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

for items in d:
    print items, d[items]

''' Result

A 230
C 220
T 242
G 252
'''
