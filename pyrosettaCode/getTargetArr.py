import os
import numpy as np
saveDir='../data/data/proteinStructure/TargetFeature/'
featureDir='../data/data/proteinStructure/structureFeature_All/'
ProteinTarget=os.listdir(featureDir)
for target in ProteinTarget: #H00001
    targetArr=None
    fileList=sorted(os.listdir(featureDir+target),key=lambda x:int((x.split('.')[0]).split('_')[1])) #H00088_3.npy
    for i,featureFile in enumerate(fileList):
        arr=np.load(featureDir+target+'/'+featureFile)
        if i==0:
            targetArr=arr
        else:
            targetArr=np.concatenate((targetArr,arr),axis=0)
    np.save(saveDir+target+'.npy',targetArr)

print('success')
