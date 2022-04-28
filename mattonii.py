#coding:UTF-8
import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


dataFile = 'mouse1.mat'
data = scio.loadmat(dataFile)

data_array = data['Mouse']
data_array = np.clip(data_array, -1000, 500)

data_array = data_array[::-1, ::-1, ::-1]
seg_array = np.transpose(data_array,(2,1,0))
out = sitk.GetImageFromArray(seg_array)
sitk.WriteImage(out,'save1.nii.gz')

# 进行可视化
#plt.imshow(seg_array) 
#plt.show()

