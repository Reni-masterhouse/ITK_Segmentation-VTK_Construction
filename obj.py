from re import U
from path import Path
import scipy.io as scio
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import mcubes

file = 'spleenseg.nii.gz'
path = sitk.ReadImage(file)
u = sitk.GetArrayFromImage(path)

vertices, triangles = mcubes.marching_cubes(u, 0.5)

#mcubes.export_obj(vertices, triangles, 'lung.obj')

smoothed_sphere = mcubes.smooth(u)
vertices, triangles = mcubes.marching_cubes(smoothed_sphere, 0)
mcubes.export_obj(vertices, triangles, 'spleen.obj')