import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

img=sitk.ReadImage('lung_seg.nii.gz')
sitk.WriteImage(img, 'lung_seg.dicom')