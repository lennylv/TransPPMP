'''
Type of mutation residue. Using a 20-dimensional one-hot vector representation of residue at the mutation site, 
we hold the opinion that mutations occur in certain residues might be more likely to cause disease.
'''
import os
import numpy as np
residueDict={'A':0,  'C':1,  'D':2,  'E':3,  'F':4,  'G':5,  'H':6,  'I':7,  'K':8, 'L':9, 
             'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19}
saveDir='../data/data/train/ESP/NS/onehot_MutationType/'
splitSeqDir='../data/data/train/ESP/NS/splitSeq/'

sequenceFileList=os.listdir(splitSeqDir)
for sequenceFile in sequenceFileList:
    with open(splitSeqDir+sequenceFile,'r') as f:
        sequence=f.read()
    Atype=residueDict[sequence[16]]
    Atype=np.eye(20)[Atype]
    np.save(saveDir+sequenceFile[:-4]+'.npy',Atype)

