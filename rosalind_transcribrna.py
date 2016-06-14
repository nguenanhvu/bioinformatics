#rosalind_rna.txt
#Objective: produce a mRNA sequence from a DNA coding sequence

'''This task could be confusing to those who are not pretty sure about the
term between coding sequence and template sequence. Template sequence is
the one to which RNA polymerase binds and start transription. Coding sequence is
complementary to the template sequence, in other words opposite to the template
sequence. The point is that coding sequence refers to as mRNA-like strand since
it is identical to mRNA stand, except "T" in coding one becoming "T" in
mRNA one'''

'''For example:
Coding strand:   3' - ATTGCGCGGCGATAT - 5'
Template strand: 5' - TAACGCGCCGCTATA - 3'
mRNA strand:     3' - AUUGCGCGGCGAUAU - 5'

You can see the similarity between coding strand and mRNA one as I described
Note that transcription will start in 5-end to 3-end direction'''

import os
os.chdir('/home/vu/Downloads/')
f = open('rosalind_rna.txt', 'r').read()[:-1]
f = f.replace('T', 'U')
print f

'''Result

UCGCGAGAGAGCAAGUGACCAUUGGGGUUCCCUAUUCAACGAUUCCUUCUUUUAGCGACAUAUUGGGUUCAAUGGGU
GCAGCAACCCUACACGUUACCCUAACAAUACAUUAUCUUCCAUGGGGGUAGCGGCUGAAGGCUGGCAACCUAAAAAA
GGAUCGCGCUUCCAGAUAGUAACACACCAGGCCUUACGUCAGACGGGUGCUCAGAGGCAAGUGAUUAUCAUGGUAUA
AGACAGAAUGGUUCGAGGGCAUCGAGACAGACGCAGCAUGAAAUAAUCACGACCCGAAUCAGAGUUCGCGCGAUUCG
CACAGUACCGCGCGCCGGAUGUGCCCGAGGAGGUUCCUUUCAGCCUGAUGUGUUCAUGCUAAUAUUGUGUUGCAUAC
AGAACUCUAGGGACGUUGUGGUAUCUAUGGGAUGGCGCGCCUUCACUCUCGGUUAGUACGUCGUAGCUGCCCGAUUA
CUACAUCGGCUAUAAGAGCGACCUGGCGAUAGAACACGGAAUAAAUCCCUAAGCCUAAGGUUUCGCAUGGCAGGUUU
UUCGGACGCUGGAACUGAGACUCGUCUUGACAGUGCGCGCAGUAAGUGUUGAGGGCCAUAAACAACGCGAUACAGGC
CCCGUCUGAUACUUACUCGGGAUUGUUUGGACAUUGUUAAGAUGAUUAGCUAGAGUUAGUAUGGGAGUGGGAUUCAG
AUUAGAUAGCCGACAUGAGCGGCACGGAACAUAAUACAAUGGAACCAAUGAGCUAUACUAAGAAUAUGGCAUUUGAG
UGGCACGUCCGUCAAGCAGGAUUAAAGUCUCGUCCAAUGUCUCCAUGCGGCAUGAGGAACUUCCCCUAGCAUUUGCC
UUCGUGUUGGCGCGUGUUUUGUGCUAGCGUGACAUCCGUCCGGUCCGCUGGUUAUUAUCUUCGAG'''