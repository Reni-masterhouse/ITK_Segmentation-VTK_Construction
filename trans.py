from path import Path
import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

file = 'lung_seg.nii.gz'
path = sitk.ReadImage(file)
data_array = sitk.GetArrayFromImage(path)

data_array = data_array[::-1, ::-1, ::-1]
out = sitk.GetImageFromArray(data_array)
sitk.WriteImage(out,'lungseg.nii.gz')