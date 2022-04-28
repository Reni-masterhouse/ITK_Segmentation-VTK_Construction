import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

dataFile = 'mouse1.mat'
data = scio.loadmat(dataFile)

data_array = data['Mouse']

#切片
#data_slice = data_array[:, :, 100]
data_slice = np.clip(data_array, -1000, 500)

#plt.hist(data_slice, bins = 20)
#plt.show()

# 加窗
def window(data_slice):
    data_slice [data_slice  <= -550] = 255
    data_slice [data_slice  >= -150] = 255
    data_slice[np.logical_and(data_slice < -150, data_slice > -550)] = 0
    return data_slice

# 归一化
#def normalazation(data_slice):
    #max = np.max(data_slice)
    #min = np.min(data_slice)
    #data_slice = (data_slice - min) / (max - min) 
    #print(data_slice)
    #avg = data_slice.mean()
    #data_slice = data_slice - avg
    #return data_slice  

data_fixed = window(data_slice)

#data_prepared = normalazation(data_slice)
#data_fixed = 255 * data_prepared

# 进行可视化
#plt.imshow(data_fixed[150,:,:], cmap=plt.cm.bone)
#plt.show()
#plt.imshow(data_fixed[:,150,:], cmap=plt.cm.bone)
#plt.show()
#plt.imshow(data_fixed[:,:,100])
plt.imshow(data_fixed[:,:,100], cmap = plt.cm.gray)
plt.show()