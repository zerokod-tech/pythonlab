# -*- coding: utf-8 -*-
"""MSDA201 Machine Learning (Multi-class classification Keras - PCA).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B4mnag-Kh_Djn9pYcb_120y_vWfm_YBX
"""

from keras.datasets import cifar10
import numpy as np

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('Traning data shape:', x_train.shape)
print('Testing data shape:', x_test.shape)

print(y_train.shape,y_test.shape)

# Find the unique numbers from the train labels
classes = np.unique(y_train)
nClasses = len(classes)
print('Total number of outputs : ', nClasses)
print('Output classes : ', classes)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt

# %matplotlib inline
label_dict = {
 0: 'airplane',
 1: 'automobile',
 2: 'bird',
 3: 'cat',
 4: 'deer',
 5: 'dog',
 6: 'frog',
 7: 'horse',
 8: 'ship',
 9: 'truck',
}
plt.figure(figsize=[5,5])

# Display the first image in training data
plt.subplot(121)
curr_img = np.reshape(x_train[0], (32,32,3))
plt.imshow(curr_img)
print(plt.title("(Label: " + str(label_dict[y_train[0][0]]) + ")"))

# Display the first image in testing data
plt.subplot(122)
curr_img = np.reshape(x_test[0],(32,32,3))
plt.imshow(curr_img)
print(plt.title("(Label: " + str(label_dict[y_test[0][0]]) + ")"))

from keras.models import Sequential
from keras.layers import Dense
from keras import utils
from keras.optimizers import RMSprop

#  convert your training and testing labels to one-hot encoding vector
y_train_cat = utils.to_categorical(y_train)
y_test_cat = utils.to_categorical(y_test)

# params
batch_size = 128
num_classes = 10
epochs = 20

# model definition
model = Sequential()
model.add(Dense(1024, activation='relu', input_shape=(3072,)))
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.summary()

#normalize
x_train = x_train/255.0
x_test = x_test/255.0
x_train_flat = x_train.reshape(-1,3072)
x_test_flat = x_test.reshape(-1,3072)

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train_flat, y_train_cat, batch_size=batch_size,epochs=epochs,verbose=1,
                    validation_data=(x_test_flat, y_test_cat))

# lets' do it with PCA
import pandas as pd

x_train = x_train/255.0
x_test = x_test/255.0
x_train_flat = x_train.reshape(-1,3072)
x_test_flat = x_test.reshape(-1,3072)

feat_cols = ['pixel'+str(i) for i in range(x_train_flat.shape[1])]
df_cifar = pd.DataFrame(x_train_flat,columns=feat_cols)
df_cifar['label'] = y_train
print('Size of the dataframe: {}'.format(df_cifar.shape))
df_cifar.head()

# fit 2 compnent PCA on cifar dataset
from sklearn.decomposition import PCA
pca_cifar = PCA(n_components=2)
principalComponents_cifar = pca_cifar.fit_transform(df_cifar.iloc[:,:-1])

principal_cifar_Df = pd.DataFrame(data = principalComponents_cifar
             , columns = ['principal component 1', 'principal component 2'])
principal_cifar_Df['y'] = y_train
principal_cifar_Df.head()

print('Explained variation per principal component: {}'.format(pca_cifar.explained_variance_ratio_))

# not enough

# perform actual PCA for training
pca = PCA(0.9)
pca.fit(x_train_flat)

pca.n_components_

train_img_pca = pca.transform(x_train_flat)
test_img_pca = pca.transform(x_test_flat)

from keras.models import Sequential
from keras.layers import Dense
from keras import utils
from keras.optimizers import RMSprop

#  convert your training and testing labels to one-hot encoding vector
y_train_cat = utils.to_categorical(y_train)
y_test_cat = utils.to_categorical(y_test)

# params
batch_size = 128
num_classes = 10
epochs = 20

# model definition
model = Sequential()
model.add(Dense(1024, activation='relu', input_shape=(99,)))
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(train_img_pca, y_train_cat,batch_size=batch_size,epochs=epochs,verbose=1,
                    validation_data=(test_img_pca, y_test_cat))

