import numpy as np
from sklearn.metrics import matthews_corrcoef,f1_score
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib

def func(Y_True,Y_Pred):
    tn,fp,fn,tp = confusion_matrix(Y_True,Y_Pred).ravel()
    print("Matthews: "+str(matthews_corrcoef(Y_True,Y_Pred)))
    print('sensitivity/recall:',tp/(tp+fn))
    print('specificity:',tn/(tn+fp))
    print("F1: "+str(f1_score(Y_True,Y_Pred)))
    print('false positive rate:',fp/(tn+fp))
    print('false discovery rate:',fp/(tp+fp))
    print('TN:',tn,'FP:',fp,'FN:',fn,'TP:',tp)

test_feature=np.load('./data/test/test_feature.npy')
test_x=test_feature[:,:-1]
test_y=test_feature[:,-1]
clf_1 = joblib.load("./train_model_1.m")
clf_2 = joblib.load("./train_model_2.m")
pred_y_1=clf_1.predict(test_x)
pred_y_2=clf_2.predict(test_x)
pred_y=(pred_y_1+pred_y_2)/2
pred_y_new=[]
for value in pred_y:
    if value<0.5:
        pred_y_new.append(0)
    else:
        pred_y_new.append(1)
pred_y_new=np.array(pred_y_new)
func(test_y,pred_y_new)