'''
Generate protein sequences from protein id
'''
import os
import numpy as np
from Bio import Entrez
from Bio import SeqIO
Entrez.email = 'email@###'

readfile='../data/data/vest_indel_test/pathogenic/vest_test_path.lst'
saveDir='../data/data/vest_indel_test/pathogenic/seq/'

idList=set()
with open(readfile,'r') as f:
    for line in f.readlines():
        idList.add(line.split()[0]) 
idList=list(idList)
print(len(idList))

for protein_id in idList:
    output_file=saveDir+protein_id+'.fasta'
    result_handle = Entrez.efetch(db="protein", rettype="gb", id=protein_id)
    seqRecord = SeqIO.read(result_handle, format='gb')
    result_handle.close()
    with open(output_file,'w') as f:
        f.write(seqRecord.format('fasta'))
