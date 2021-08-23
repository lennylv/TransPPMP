'''
Percentage affected
'''
import numpy as np
import os
from Bio import SeqIO

# Reading fasta sequences
def readFasta(file):
    fa_seq = SeqIO.read(file, "fasta")
    return fa_seq.seq

readfile='../data/data/train/ESP/NS/NS_esp.lst'
seqFile='../data/data/train/ESP/NS/seq/'
saveDir='../data/data/train/ESP/NS/fraction/'
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],line.split()[1]
        sequence=readFasta(seqFile+filename+'.fasta')
        Nr=float(len(sequence))
        k=float(position)
        rate=(Nr-k+1.0)/Nr
        savesplitSequenceFile=saveDir+filename+'_'+position+'.npy'
        if os.path.exists(savesplitSequenceFile):
            print(savesplitSequenceFile)
        else:
            np.save(savesplitSequenceFile,np.array([rate]))