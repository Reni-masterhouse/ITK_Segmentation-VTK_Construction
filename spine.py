import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 加窗
def window(img):
    win_min = 205
    win_max = 255

    for i in range(img.shape[0]):
        img[i] = 255.0*(img[i] - win_min)/(win_max - win_min)
        min_index = img[i] < 0
        img[i][min_index] = 0
        max_index = img[i] > 255
        img[i][max_index] = 255       
        img[i] = img[i] - img[i].min()
        c = float(255)/img[i].max()
        img[i] = img[i]*c
    
    return img.astype(np.uint8)



img = sitk.ReadImage('save.nii.gz')
img = sitk.GetArrayFromImage(img)   
img = window(img)

out = sitk.GetImageFromArray(img)
sitk.WriteImage(out,'spine.nii.gz')
