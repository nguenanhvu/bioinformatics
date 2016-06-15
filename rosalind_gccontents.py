#GC contents
#Count the GC contents in given sequences and list the greatest value

import os
os.chdir('/home/vu/Downloads')
f = open('rosalind_gc (2).txt', 'r').read().split('>')
d = {}

for i in f:
    if i == '':
        pass
    else:
        h = i.split('\n')
        header = h[0]
        sequence = ''.join(h[1:])
        A = sequence.count('A')
        T = sequence.count('T')
        G = sequence.count('G')
        C = sequence.count('C')
        total_nucleotide = A + T + G + C
        GC_contents = (float(G+C)/total_nucleotide)*100
        d[header] = GC_contents

print max(d.items(), key=lambda k: k[1]) #determine the greatest value

'''Result
'Rosalind_1491', 52.74356103023516
'''

