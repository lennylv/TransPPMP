import tensorflow as tf
import numpy as np
from model import get_model
import os
from sklearn.utils import class_weight
#批量梯度下降,迭代训练模型
# class_weights=class_weight.compute_class_weight('balanced',np.unique(train_y),train_y)
# reduceLR=tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss',factor=0.2,patience=5)

def train():
    trainFeature=np.lib.format.open_memmap('./DataAndCode/data/trainNpy/train_feature.npy')
    trainESM=np.lib.format.open_memmap('./DataAndCode/data/trainNpy/train_esm.npy')

    L=trainFeature.shape[0]
    shuffleIndex=list(range(L))
    np.random.shuffle(shuffleIndex)

    trainFeature=trainFeature[shuffleIndex]
    trainESM=trainESM[shuffleIndex]

    train_feature=trainFeature[:,33:-1]
    train_y=trainFeature[:,-1]
    
    qa_model=get_model()
    valiBestModel = './model.h5'
    checkpoiner=tf.keras.callbacks.ModelCheckpoint(filepath=valiBestModel,monitor='val_loss',save_weights_only=True,verbose=1,save_best_only=True)
    earlyStopPatience = 10
    earlystopping=tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=earlyStopPatience,verbose=0,mode='auto')

    log_dir="logs/fit/model/sequenceModel"
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, write_graph=True)

    history_callback=qa_model.fit(
        x=[trainESM,train_feature], 
        y=train_y, 
        batch_size=128, 
        epochs=10000, 
        verbose=1, 
        callbacks=[checkpoiner,earlystopping], 
        validation_split=0.1, 
        shuffle=True,
    )
    
if __name__=="__main__":
    os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
    config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(allow_growth=True))
    sess = tf.compat.v1.Session(config=config)
    train()




