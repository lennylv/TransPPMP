'''
Obtaining PSSM from HHM [N,30]
'''
import argparse,os
import itertools
import numpy as np
import scipy.io as sio
from scipy.spatial.distance import pdist, squareform
from Bio import SeqIO

def readFasta(file):
    fa_seq = SeqIO.read(file, "fasta")
    return fa_seq.seq

def extract_hmm_profile(hhm_file, sequence, asterisks_replace=0.0):
    """Extracts information from the hmm file and replaces asterisks."""
    profile_part = hhm_file.split('#')[-1]
    profile_part = profile_part.split('\n')
    whole_profile = [i.split() for i in profile_part]
    # This part strips away the header and the footer.
    whole_profile = whole_profile[5:-2]
    gap_profile = np.zeros((len(sequence), 10))
    aa_profile = np.zeros((len(sequence), 20))
    count_aa = 0
    count_gap = 0
    for line_values in whole_profile:
        if len(line_values) == 23:
            # The first and the last values in line_values are metadata, skip them.
            for j, t in enumerate(line_values[2:-1]):
                aa_profile[count_aa, j] = (2**(-float(t) / 1000.) if t != '*' else asterisks_replace)
            count_aa += 1
        elif len(line_values) == 10:
            for j, t in enumerate(line_values):
                gap_profile[count_gap, j] = (2**(-float(t) / 1000.) if t != '*' else asterisks_replace)
            count_gap += 1
        elif not line_values:
            pass
        else:
            raise ValueError('Wrong length of line %s hhm file. Expected 0, 10 or 23'
                           'got %d'%(line_values, len(line_values)))
    hmm_profile = np.hstack([aa_profile, gap_profile])
    assert len(hmm_profile) == len(sequence)
    return hmm_profile

HHMDir='/mnt/sdc/user/nlp/hh-suite/build/HHM/'
saveDir='/mnt/sdc/user/nlp/protein_mutation/DataAndCode/data/data/pssm/'
typeList=os.listdir(HHMDir)
for type in typeList:       
    os.mkdir(saveDir+type)
    hhmList=os.listdir(HHMDir+type)
    for hhmName in hhmList:# NP_000141.1.hhm
        hhmFile=HHMDir+type+'/'+hhmName
        with open(hhmFile,'r') as f:
            mytxt=f.read()

        sequence=readFasta('/mnt/sdc/user/nlp/hh-suite/build/sequence/'+type+'/'+hhmName[:-3]+'fasta')
        q=extract_hmm_profile(mytxt, sequence, asterisks_replace=0.0)
        np.save(saveDir+type+'/'+hhmName[:-3]+'npy',q)
