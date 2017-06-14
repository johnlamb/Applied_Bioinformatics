#!/usr/bin/env python3
import sys
import random

alphabet = 'ACGT'
alphabet_weights = [1,1,1,1]
prot_id = 'mysequence'

if len(sys.argv) > 1:
    if sys.argv[1] == '-h':
        print("Usage: ./randomdna.py <alphabet> <alphabet_weights> <prot_id>")
        print("alphabet is a string of the possible letters with no separator")
        print("If alphabet_weights are given they must be a comma separated list of the same length as the alphabet")
        sys.exit()
    alphabet = sys.argv[1]
    if len(sys.argv) > 2:
        alphabet_weights = [int(i) for i in sys.argv[2].split(',')]
    if len(sys.argv) > 3:
        prot_id = sys.argv[3]

if len(alphabet) != len(alphabet_weights):
    print("alphabet and alphabet_weights must be of the same length")
    sys.exit()
#assert len(alphabet) == len(alphabet_weights)

len_fasta = input("Length: ")
print("")

accession = '>' + prot_id

c = random.choices(alphabet, weights=alphabet_weights, k=int(len_fasta))
seq = ''.join(c)

fastaoutput = accession + '\n' + seq + '\n'

print(fastaoutput)
