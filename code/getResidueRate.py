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
    for residueInfo in proteinArr:
        if residueInfo[0]==position:
            mutationPositionXYZ=residueInfo[2:5]
            break
    if mutationPositionXYZ is None:
        localArr=[0]*20
        localArr=np.array(localArr)
    else:
        localArr=[0]*20
        for residueInfo in proteinArr:
            result=getDist(residueInfo[2:5],mutationPositionXYZ)
            if 0<result and result<=12:
                localArr[int(residueInfo[1])]+=1
        localArr=np.array(localArr)
        localArr=localArr/sum(localArr)
    return localArr
def getMap(file):
    map={}
    with open(file,'r') as f:
        for line in f.readlines():
            arr=line.split()
            map[arr[0]]=arr[1]
    return map

readmeFile='../data/data/proteinStructure/readme.blast'
TargetFeatureDir='../data/data/proteinStructure/TargetPDB/'

readfile='../data/data/vest_indel_test/pathogenic/vest_test_path.lst'
saveDir='../data/data/vest_indel_test/pathogenic/residueRate/'
map=getMap(readmeFile)
with open(readfile,'r') as f:
    for line in f.readlines():
        filename,position=line.split()[0],int(line.split()[1])
        mapProtein=map[filename]
        proteinArr=np.load(TargetFeatureDir+mapProtein+'/'+mapProtein+'.npy')
        localArr=getLocalInfo(proteinArr,position)
        mySaveFile=saveDir+filename+'_'+str(position)+'.npy'
        if os.path.exists(mySaveFile):
            print(mySaveFile)
        else:
            np.save(mySaveFile,localArr)
           
