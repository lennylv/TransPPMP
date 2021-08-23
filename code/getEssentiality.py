'''
Obtain the importance of mutation samples
'''
import os
import numpy as np

def getMap(file):
    map={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            map[arr[0]]=arr[1]
    return map

def getEssentialityProteinList(file):
    proteinList=[]
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            proteinList.append(arr[1])
    return proteinList

readmeFile='../data/data/proteinStructure/readme.blast'
map=getMap(readmeFile)
ProteinEssentialityFile='../data/data/proteinStructure/human_map2essential.lst'
proteinList=getEssentialityProteinList(ProteinEssentialityFile)

readfile='../data/data/vest_indel_test/pathogenic/vest_test_path.lst'
saveDir='../data/data/vest_indel_test/pathogenic/Essentiality/'
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],line.split()[1]
        proteinName=map[filename]
        if proteinName in proteinList:
            arr=np.array([1])
        else:
            arr=np.array([0])
        savesplitSequenceFile=saveDir+filename+'_'+position+'.npy'
        if os.path.exists(savesplitSequenceFile):
            print(savesplitSequenceFile)
        else:
            np.save(savesplitSequenceFile,arr)