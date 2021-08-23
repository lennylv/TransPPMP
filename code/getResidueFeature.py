import os
import numpy as np
def construct_residue_level_feature(residue):
    def AAcharge(AA):       
        if AA in ['D','E']:
            return -1.
        elif AA in ['R','H','K']:
            return 1.
        else:
            return 0.
    residueFeature = []
    Hydro = ['A', 'V', 'I', 'L', 'M', 'F', 'Y', 'W'] 
    PolarAll = ['S','T','N','Q','R','H','K','D','E'] 
    PolarUncharged = ['S','T','N','Q']               
    PolarPosCharged = ['R','H','K']                  
    PolarNegCharged = ['D','E']                      
    SpecialCase = ['C','U','G','P']
    AAvolume = {'A': 0.16994633273703036, 'R': 0.6756112104949314, 'D': 0.3041144901610017, 'N': 0.32200357781753125, 'C': 0.2886106141920095, 'E': 0.4669051878354204, 'Q': 0.4991055456171736, 'G': 0.0, 'H': 0.5551580202742993, 'I': 0.6356589147286821, 'L': 0.6356589147286821, 'K': 0.6469886702444841, 'M': 0.6129994036970782, 'F': 0.7740011926058438, 'P': 0.31365533691115083, 'S': 0.17233154442456766, 'T': 0.3339296362552176, 'W': 1.0, 'Y': 0.7960644007155634, 'V': 0.47644603458556944,'U':0}
    AAhydropathy = {'A': 0.7, 'R': 0.0, 'N': 0.1111111111111111, 'D': 0.1111111111111111, 'C': 0.7777777777777778, 'E': 0.1111111111111111, 'Q': 0.1111111111111111, 'G': 0.4555555555555555, 'H': 0.14444444444444443, 'I': 1.0, 'L': 0.9222222222222223, 'K': 0.06666666666666668, 'M': 0.7111111111111111, 'F': 0.8111111111111111, 'P': 0.3222222222222222, 'S': 0.41111111111111115, 'T': 0.4222222222222222, 'W': 0.4, 'Y': 0.35555555555555557, 'V': 0.9666666666666666,'U':0}
    AAarea = {'A': 0.2222222222222222, 'R': 0.8333333333333334, 'D': 0.4166666666666667, 'N': 0.4722222222222222, 'C': 0.3333333333333333, 'E': 0.6388888888888888, 'Q': 0.5833333333333334, 'G': 0.0, 'H': 0.6666666666666666, 'I': 0.5555555555555556, 'L': 0.5277777777777778, 'K': 0.6944444444444444, 'M': 0.6111111111111112, 'F': 0.75, 'P': 0.3888888888888889, 'S': 0.2222222222222222, 'T': 0.3611111111111111, 'W': 1.0, 'Y': 0.8611111111111112, 'V': 0.4444444444444444,'U':0}
    AAweight = {'A': 0.10860089345855174, 'R': 0.7675381887721526, 'N': 0.4417122815710625, 'D': 0.44933842258886214, 'C': 0.3568182346064215, 'E': 0.5579393160474138, 'Q': 0.5503131750296142, 'G': 0.0, 'H': 0.620071074085831, 'I': 0.4344035738342071, 'L': 0.4344035738342071, 'K': 0.5506460928608481, 'M': 0.5740200215235249, 'F': 0.6977725474407911, 'P': 0.3101942536833875, 'S': 0.23246955350299248, 'T': 0.3410704469615442, 'W': 1.0, 'Y': 0.8216412074852317, 'V': 0.3258026803756552,'U':0}
    Groups = [Hydro, PolarAll, PolarUncharged, PolarPosCharged, PolarNegCharged, SpecialCase]
    AA = residue
    for Group in Groups:
        if AA in Group:
            residueFeature.append(1.0)
        else:
            residueFeature.append(0.0)
    residueFeature.append(AAvolume[AA])
    residueFeature.append(AAhydropathy[AA])
    residueFeature.append(AAarea[AA])
    residueFeature.append(AAweight[AA])
    residueFeature.append(AAcharge(AA))

    return residueFeature

def getResidueFeature(sequence):
    result=[]
    for residue in sequence:
        if residue in ['#']:
            residueFeature=[0]*11
        else:
            residueFeature=construct_residue_level_feature(residue)
        result.append(residueFeature)
    result=np.array(result)
    return result

path='../data/data/vest_indel_test/pathogenic/'

splitSeqDir=path+'splitSeq100/'
saveDir=path+'residueFeature100/'
os.mkdir(saveDir)

sequenceFileList=os.listdir(splitSeqDir)
for sequenceFile in sequenceFileList:
    with open(splitSeqDir+sequenceFile,'r') as f:
        sequence=f.read()
    result=getResidueFeature(sequence)
    np.save(saveDir+sequenceFile[:-3]+'npy',result)


