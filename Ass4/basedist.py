#!/usr/bin/env python3
import argparse
import math
import sys
parser = argparse.ArgumentParser()

parser.add_argument('files', nargs='+', help='list of file names')
args = parser.parse_args()

def readFasta(fileName):
    """Reads a fasta file and returns a dict with IDs as keys"""
    prots = {}
    try:
        with open(fileName) as ofile:
            pid = ''
            seq = ''
            for line in ofile:
                if line[0] == '>':
                    if len(seq)>0:
                        prots[pid] = seq
                        seq = ''
                    pid = line[1:].split(' ')[0].strip()
                else:
                    seq += line.upper().strip()
            if len(seq)>0:
                prots[pid] = seq
                seq = ''
        return prots
    except:
        print("No such file")
        sys.exit()

def composition(dna):
    total_len = len(dna)
    comp = []
    for c in 'ACGT':
        comp.append(dna.count(c)/total_len)
    return comp

def comp_diff(comp1, comp2):
    l = len(comp1)
    total_sum = 0
    for i in range(l):
        total_sum += (comp1[i]-comp2[i])**2
    return(math.sqrt(total_sum/4))

def print_mat(species, mat):
    num_species = len(species)
    print(num_species)
    for i in range(num_species):
        print("{:<10s}".format(species[i][:10]),end='')
        for dist in mat[i]:
            print("{0:.3f}".format(dist), end='\t')
        print('\n')

name_list = []
comp_list = []
for f in args.files:
    for key, seq in readFasta(f).items():
        name_list.append(key)
        comp_list.append(composition(seq))
mat = []
list_len = len(name_list)
for i in range(list_len):
    temp_row = []
    for j in range(list_len):
        temp_row.append(comp_diff(comp_list[i], comp_list[j]))
    mat.append(temp_row)
print_mat(name_list, mat)
