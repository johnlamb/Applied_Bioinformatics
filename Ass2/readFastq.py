#!/usr/bin/env python3
import sys

if len(sys.argv) == 1 or sys.argv[1] == '-h':
    print("Usage: ./readFastq.py inputfile")
    sys.exit()

fileName = sys.argv[1]
num_seq = 0
accessions = []
with open(fileName) as ofile:
    for i, line in enumerate(ofile):
        if i%4 == 0:
            num_seq += 1
            accessions.append(line[1:])

print(num_seq)
for accession in accessions:
    print(accession,end='')
