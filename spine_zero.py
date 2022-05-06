import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = sitk.ReadImage('spine_seg.nii.gz')
img = sitk.GetArrayFromImage(img)   
    
img[:, :, 0] = 0
img[:, :, -1] = 0
img[0, :, :] = 0
img[-1, :, :] = 0
img[:, 0, :] = 0
img[:, -1, :] = 0

out = sitk.GetImageFromArray(img)
sitk.WriteImage(out,'spine_zero.nii.gz')
