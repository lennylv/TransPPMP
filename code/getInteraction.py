'''
Number of protein interactions
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
    proteinMap={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            proteinMap[arr[0]]=float(arr[1])
    return proteinMap

readmeFile='../data/data/proteinStructure/readme.blast'
map=getMap(readmeFile)
ProteinInteractionFile='../data/data/proteinStructure/list_node.lst'
proteinMap=getEssentialityProteinList(ProteinInteractionFile)

readfile='../data/data/vest_indel_test/pathogenic/vest_test_path.lst'
saveDir='../data/data/vest_indel_test/pathogenic/Interaction/'
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],int(line.split()[1])
        ProteinName=map[filename]
        geshu=proteinMap[ProteinName]
        mylen=np.array([geshu])
        mySaveFile=saveDir+filename+'_'+str(position)+'.npy'
        if not os.path.exists(mySaveFile):
            np.save(mySaveFile,mylen)
            print(mylen)
