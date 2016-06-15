#Counting point mutation
#Objective: counting hammer distance
'''Hammer distance is the sum of different points between 2 DNA strands'''

import os
os.chdir('/home/vu/Downloads')
f = open('rosalind_hamm (1).txt', 'r').read().split('\n')
sequence1 = f[0]
sequence2 = f[1]
d = []
n = 0

for i in sequence1:
    if sequence1[n] == sequence2[n]:
        n+=1
        pass
    elif sequence1[n] != sequence2[n]:
        d.append(sequence1[n])
        n+=1
t = 0
for items in d:
    t+=1
print t
    
'''Result
448'''


