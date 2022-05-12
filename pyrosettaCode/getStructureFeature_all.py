import numpy as np
import os
def getEnergies(energiesTxtFile):
    saveNpy=[]
    with open(energiesTxtFile,'r') as f:

        LineList=[line for line in f]

        LineList=LineList[1:-1]
        for line in LineList:

            energies=line.split()[1:]

            energies=list(map(float,energies))

            saveNpy.append(energies)
            
    saveNpy=np.array(saveNpy)
    return saveNpy


structureFeatureDir='../data/data/proteinStructure/structureFeature/'               
structureEnergiesDir='../data/data/proteinStructure/structureEnergiesFile/'    
structureFeatureAllDir='../data/data/proteinStructure/structureFeature_All/'

targetList=os.listdir(structureFeatureDir)
for target in targetList:  
    os.mkdir(structureFeatureAllDir+target)

    structureList=os.listdir(structureFeatureDir+target)
    for structure in structureList:#xxx_1.npy
        structureName=structure.split('.')[0]
        featureFile=structureFeatureDir+target+'/'+structure  
        featureNpy=np.load(featureFile)
        structureEnergiesFile=structureEnergiesDir+target+'/'+structureName+'.txt'
        #
        structureFeatureAllFile=structureFeatureAllDir+target+'/'+structure
        if os.path.exists(structureEnergiesFile):
            energiesNpy=getEnergies(structureEnergiesFile)

        else:
            print('NOT EXISTS:'+structureEnergiesFile)
            n=len(featureNpy)
            energiesNpy=[[0]*19 for i in range(n)]
            energiesNpy=np.array(energiesNpy)
        featureAllNpy=np.concatenate((featureNpy[:,0:25],energiesNpy,featureNpy[:,25:]),axis=1)
        np.save(structureFeatureAllFile,featureAllNpy)
print('END')






