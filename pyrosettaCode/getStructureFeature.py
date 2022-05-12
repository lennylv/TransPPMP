import os,sys
import numpy as np
from pyrosetta import *
init()

residueDict={'A':0,  'C':1,  'D':2,  'E':3,  'F':4,  'G':5,  'H':6,  'I':7,  'K':8, 'L':9, 
             'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19,'U':20}
ssDict={'H':0,'E':1,'L':2}

structureDir='../data/data/proteinStructure/proteinPdbStructure/'                    
structureFeatureDir='../data/data/proteinStructure/structureFeature/'               
structureEnergiesDir='../data/data/proteinStructure/structureEnergiesFile/'          

targetList=os.listdir(structureDir)
split1=targetList[0:300]
split2=targetList[300:600]
split3=targetList[600:900]
split4=targetList[900:1200]
split5=targetList[1200:1500]
split6=targetList[1500:1800]
split7=targetList[1800:2100]
split8=targetList[2100:2400]
split9=targetList[2400:2700]
split10=targetList[2700:3000]
split11=targetList[3000:3300]
split12=targetList[3300:3600]
split13=targetList[3600:3900]
split14=targetList[3900:4200]
split15=targetList[4200:4500]
split16=targetList[4500:4800]
split17=targetList[4800:5100]
split18=targetList[5100:5400]
split19=targetList[5400:5700]
split20=targetList[5700:6000]
split21=targetList[6000:]

for target in split21:                                    
    os.mkdir(structureFeatureDir+target)
    os.mkdir(structureEnergiesDir+target)
    structureList=os.listdir(structureDir+target)

    for structure in structureList:

        structureFile=structureDir+target+'/'+structure                                           
        saveStructureFeatureFile=structureFeatureDir+target+'/'+structure.split('.')[0]+'.npy'             
        saveEnergiesFile=structureEnergiesDir+target+'/'+structure.split('.')[0]+'.txt'

        structurePose=pose_from_pdb(structureFile)
        #position
        positionList=[]
        n=structurePose.pdb_info().nres()
        for i in range(1,n+1):
            positionList.append(structurePose.pdb_info().number(i))
        positionList=np.array(positionList).reshape(-1,1)
        #SEQUENCE
        sequence=structurePose.sequence()
        sequenceList=list(sequence)
        sequenceToInt=[]
        for res in sequenceList:
            Atype=residueDict[res]
            Atype=np.eye(21)[Atype]
            sequenceToInt.append(Atype)
        sequenceToInt=np.array(sequenceToInt)
        #SS
        try:
            structurePose.display_secstruct()
            SS=structurePose.secstruct()
            SSList=list(SS)
            SSToInt=[]
            for type in SSList:
                stype=ssDict[type]
                stype=np.eye(3)[stype]
                SSToInt.append(stype)
            SSToInt=np.array(SSToInt)
        except Exception as e:
            SSToInt=np.zeros((len(sequence),3))
        #CA
        coorArr_CA=[]
        n=structurePose.pdb_info().nres()
        for i in range(1,n+1):
            #CA
            CA_index=structurePose.residue(i).atom_index('CA')
            CA_coor=list(map(float,str(structurePose.residue(i).atom(CA_index)).split(',')))
            coorArr_CA.append(CA_coor)

        coorArr_CA=np.array(coorArr_CA)
        #
        saveNpy=np.concatenate((positionList,sequenceToInt,SSToInt,coorArr_CA),axis=1)
        np.save(saveStructureFeatureFile,saveNpy)
        #ENERGIES
        try:
            get_fa_scorefxn()(structurePose)
            with open(saveEnergiesFile,'w') as f:
                f.write(str(structurePose.energies()))
        except Exception as e:
            print('CANNOT')

print('success')

                
                




