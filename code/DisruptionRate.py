'''
Extent of structural destruction
'''
import numpy as np
import os
import math
from Bio import SeqIO

def getDist(dot_1,dot_2):
    dot_diff=dot_1-dot_2
    a=math.hypot(dot_diff[0],dot_diff[1])
    result=math.hypot(a,dot_diff[2])
    return result

def getLocalInfo(proteinArr,position):
    mutationPositionXYZ=None
    for residueInfo in proteinArr:
        if residueInfo[0]==position:
            mutationPositionXYZ=residueInfo[2:5]
            break
    if mutationPositionXYZ is None:
        return 0
    else:
        num=0
        for residueInfo in proteinArr:
            result=getDist(residueInfo[2:5],mutationPositionXYZ)
            if 0<=result and result<=12:
                num+=1
        return num

def getMap(file):
    map={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            map[arr[0]]=arr[1]
    return map

readmeFile='../data/data/proteinStructure/readme.blast'
TargetFeatureDir='../data/data/proteinStructure/TargetPDB/'
path='../data/data/vest_indel_test/pathogenic/'
readfile=path+'vest_test_path.lst'
saveDir=path+'pohuai/'
os.mkdir(saveDir)
map=getMap(readmeFile)
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],int(line.split()[1])
        mapProtein=map[filename]
        proteinArr=np.load(TargetFeatureDir+mapProtein+'/'+mapProtein+'.npy')
        num=getLocalInfo(proteinArr,position)
        res=np.array([num/len(proteinArr)])
        mySaveFile=saveDir+filename+'_'+str(position)+'.npy'
        if os.path.exists(mySaveFile):
            print(mySaveFile)
        else:
            np.save(mySaveFile,res)
           
