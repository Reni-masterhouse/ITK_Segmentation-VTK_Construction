import vtk
import sys
 
reader = vtk.vtkNIFTIImageReader()
reader.SetFileName('liver_seg.nii.gz')
reader.Update()
print (reader)
 
contour=vtk.vtkMarchingCubes()  
contour.SetInputData(reader.GetOutput())
contour.ComputeNormalsOn()
contour.ComputeGradientsOn()
contour.SetValue(0,0.1)
contour.Update()
 
# Write in vtk
triangle = vtk.vtkTriangleFilter()
triangle.SetInputConnection(contour.GetOutputPort())
triangle.PassVertsOff()
triangle.PassLinesOff()
 
decimation=vtk.vtkQuadricDecimation()
decimation.SetInputConnection(triangle.GetOutputPort())
 
clean=vtk.vtkCleanPolyData()
clean.SetInputConnection(triangle.GetOutputPort())
 
triangle2 = vtk.vtkTriangleFilter()
triangle2.SetInputConnection(clean.GetOutputPort())
triangle2.PassVertsOff()
triangle2.PassLinesOff()
 
#save .vtk polydata
writer = vtk.vtkPolyDataWriter()
writer.SetFileTypeToASCII()
writer.SetInputConnection(contour.GetOutputPort())
writer.SetFileName("out.vti")
writer.Write()