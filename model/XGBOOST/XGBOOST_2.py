'''
XGBOOST_2
'''
import numpy as np
from xgboost import XGBRegressor
import os
from sklearn.externals import joblib
train_feature=np.load('./data/train/train_feature_2.npy')
train_x=train_feature[:,:-1]
trian_y=train_feature[:,-1]
clf = XGBRegressor(
    n_estimators=2000, 
    learning_rate=0.005,  
    max_depth=8,   
    subsample=1,  
    random_state=0,  
    tree_method='gpu_hist',
    booster='gbtree',
    eval_metric='mae',
    nthread=36,
).fit(train_x,trian_y)
joblib.dump(clf, "./train_model_2.m")


