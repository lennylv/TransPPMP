'''
Find out if the protein is associated with a disease
'''
import numpy as np
import os

def getMap(file):
    map={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            map[arr[2]]=arr[1]
    return map
#Get all disease-related proteins 
def getDiseaseProteinList(file):
    proteinList=[]
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            proteinList.append(arr[0])
    return proteinList
#Get all human diseases 
def getHumanProteinList(file):
    proteinList=[]
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            proteinList.append(arr[1])
    return proteinList
readmeFile='../data/data/proteinStructure/list_gene.lst'
map=getMap(readmeFile)
gencardFile='../data/data/proteinStructure/gencard.lst'
DiseaseProteinList=getDiseaseProteinList(gencardFile)
humanDiseaseFile='../data/data/proteinStructure/human2disease.lst'
humanProteinList=getHumanProteinList(humanDiseaseFile)

readfile='../data/data/train/ESP/NS/NS_esp.lst'
saveDir='../data/data/train/ESP/NS/Disease/'
os.mkdir(saveDir)
disnum=0
bennum=0
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],line.split()[1]
        proteinName=map[filename]
        num=0
        if proteinName in DiseaseProteinList:
            num+=1
        if filename in humanProteinList:
            num+=1
        if num>0:
            disnum+=1
        else:
            bennum+=1
        savesplitSequenceFile=saveDir+filename+'_'+position+'.npy'
        if not os.path.exists(savesplitSequenceFile):
            np.save(savesplitSequenceFile,np.array([num]))

print('pathogenic：',disnum)
print('neutral：',bennum)
