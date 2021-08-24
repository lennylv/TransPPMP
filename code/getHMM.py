'''
Generating HHM files with hhblits
hhblits -i ./NP_000141.1.fasta -ohhm ./MY.hhm -d /mnt/sdc/user/heruji/uniprot20_2016_02/uniprot20_2016_02
'''
import os
typeList=['FS_1kgen']
for myType in typeList:
    os.mkdir('./HHM/'+myType)
    fastaList=os.listdir('./sequence/'+myType)
    for fastaName in fastaList: #NP_000141.1.fasta
        fastaFile='./sequence/'+myType+'/'+fastaName
        saveFile='./HHM/'+myType+'/'+fastaName[:-6]+'.hhm'
        os.system('hhblits -i {} -ohhm {} -n 2 -d /mnt/sdc/user/heruji/uniprot20_2016_02/uniprot20_2016_02 -cpu 4'
                  .format(fastaFile,saveFile))
