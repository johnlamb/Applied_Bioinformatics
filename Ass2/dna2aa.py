#!/usr/bin/env python3
import sys
dna_trans_table = str.maketrans({ord('A'):'T',
                                 ord('T'):'A',
                                 ord('G'):'C',
                                 ord('C'):'G'})

dna_to_rna_table = str.maketrans({ord('A'):'U',
                                 ord('T'):'A',
                                 ord('G'):'C',
                                 ord('C'):'G'})

aa_table = {'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
'AAU':'N', 'AAC':'N',
'GAU':'D', 'GAC':'D',
'UGU':'C', 'UGC':'C',
'CAA':'Q', 'CAG':'Q',
'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
'CAU':'H', 'CAC':'H',
'AUU':'I', 'AUC':'I', 'AUA':'I',
'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'AAA':'K', 'AAG':'K',
'AUG':'M',
'UUU':'F', 'UUC':'F',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'UGG':'W',
'UAU':'Y', 'UAC':'Y',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'UAA':'*', 'UGA':'*', 'UAG':'*'}


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
def reverseComplement(dna):
    """Return the reverse complement of a dna string"""
    return dna.translate(dna_trans_table)[::-1]

def transcribeDNA(dna):
    """Returns the transcribed rna from a dna string"""
    return dna.translate(dna_to_rna_table)[::-1]

def translateRNA(rna, start_pos = 0):
    """Return the resulting peptide translated from a rna string"""
    curr_codon = start_pos
    seq = ''
    while curr_codon < len(rna) - 2:
        rna_codon = rna[curr_codon:curr_codon + 3]
        p = aa_table.get(rna_codon, 'X')
        seq += p
        curr_codon += 3
    return seq

def longest_ORF(dna):
    """Returns the longest ORF (peptide) in either direction of a dna string"""
    total_prots = ''
    rna = transcribeDNA(dna)
    reverse_rna = transcribeDNA(reverseComplement(dna))
    for i in range(3):
        total_prots += translateRNA(rna,i)
        total_prots += '*'
        total_prots += translateRNA(reverse_rna,i)
        total_prots += '*'
    candidates = total_prots.split('*')
    return max(candidates, key=len)

if __name__ == '__main__':
    myinput = 'translationtest.dna'
    fasta_file = input("Which file? ")
    proteins = readFasta(fasta_file)
    for key, dna in proteins.items():
        orf = longest_ORF(dna)
        print('>' + key, orf, sep='\n')
