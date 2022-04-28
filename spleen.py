import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = sitk.ReadImage('save.nii.gz')
img = sitk.GetArrayFromImage(img)   

# 加窗
#def window(img):
win_min = 0
win_max = 150

img[img>win_max] = win_min
img[img<win_min] = win_min

#img = np.clip(img, win_min, win_max)
#out = sitk.GetImageFromArray(img)
#sitk.WriteImage(out,'liver2.nii.gz')
#print(img[345,229,258])
#print(img[292,261,249])

img = 255.*(img - win_min) / (win_max - win_min)
out = sitk.GetImageFromArray(img)
sitk.WriteImage(out,'spleen.nii.gz')