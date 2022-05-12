import numpy as np
import os
import math
def getDist(dot_1,dot_2):
    dot_diff=dot_1-dot_2
    a=math.hypot(dot_diff[0],dot_diff[1])
    result=math.hypot(a,dot_diff[2])
    return result

def getLocalInfo(proteinArr,position):
    mutationPositionXYZ=None
    mutationFeature=None
    for residueInfo in proteinArr:
        if residueInfo[0]==position:
            mutationPositionXYZ=residueInfo[-3:]
            mutationFeature=residueInfo
            break
    if mutationPositionXYZ is None:
        localArr=[[0]*47 for i in range(300)]
        localArr=np.array(localArr)
    else:
        localArr=[]
        for residueInfo in proteinArr:
            result=getDist(residueInfo[-3:],mutationPositionXYZ)
            if 0<=result and result<=5:
                localArr.append(residueInfo)
        localArr=np.array(localArr)
        l=len(localArr)
        n=300-l
        padNum=np.array([[0]*47 for i in range(n)])
        localArr=np.concatenate((localArr,padNum),axis=0)

    return localArr

def getMap(file):
    map={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            map[arr[0]]=arr[1]
    return map

readmeFile='../data/data/proteinStructure/readme.blast'
TargetFeatureDir='../data/data/proteinStructure/TargetFeature/'


readfile='../data/data/vest_indel_test/pathogenic/vest_test_path.lst'
saveDir='../data/data/vest_indel_test/pathogenic/localStructureFeature/'
os.mkdir(saveDir)
map=getMap(readmeFile)
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],int(line.split()[1])
        mapProtein=map[filename]
        proteinArr=np.load(TargetFeatureDir+mapProtein+'.npy')
        localArr=getLocalInfo(proteinArr,position)
        mySaveFile=saveDir+filename+'_'+str(position)+'.npy'
        if os.path.exists(mySaveFile):
            print(mySaveFile)
        else:
            np.save(mySaveFile,localArr)
