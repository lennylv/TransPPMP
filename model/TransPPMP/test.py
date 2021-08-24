from sklearn.metrics import matthews_corrcoef,f1_score
import os
import numpy as np
from model import get_model
import tensorflow as tf
from sklearn.metrics import confusion_matrix

def test(modelFile):
    trainFeature=np.load('./DataAndCode/data/testNpy/feature.npy')
    trainESM=np.load('./DataAndCode/data/testNpy/esm.npy')

    train_feature=trainFeature[:,33:-1]
    Y_True=trainFeature[:,-1]
    #load model
    train_model=get_model()
    train_model.load_weights(modelFile)
    Y_Pred=train_model.predict([trainESM,train_feature]).reshape(-1,)
    
    Y_Pred_new=[]
    for value in Y_Pred:
        if value<0.5:
            Y_Pred_new.append(0)
        else:
            Y_Pred_new.append(1)
    Y_Pred_new=np.array(Y_Pred_new)
    tn, fp, fn, tp = confusion_matrix(Y_True, Y_Pred_new).ravel()

    print("Matthews相关系数: "+str(matthews_corrcoef(Y_True,Y_Pred_new)))
    print('sensitivity/recall:',tp/(tp+fn))
    print('specificity:',tn/(tn+fp))
    print("F1值: "+str(f1_score(Y_True,Y_Pred_new)))
    print('false positive rate:',fp/(tn+fp))
    print('false discovery rate:',fp/(tp+fp))
    print('TN:',tn,'FP:',fp,'FN:',fn,'TP:',tp)
if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"]="1"
    test('./model.h5')
