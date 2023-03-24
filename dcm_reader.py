import pydicom
import os 
import numpy as np

# DICOM directory
dir = '\dicom\'

names = os.listdir(dir)

idx = 0

# First read a single dcm slice
dcm_slice = pydicom.dcmread(os.path.join(dir, names[0]))

# Determine no. of rows, columns, and channels
n_rows = dcm_slice.Rows
n_columns = dcm_slice.Columns
n_channels = len(names)

dim = (n_rows, n_columns, n_channels)

# Create an empty array to store all slices
dcm_data = np.zeros(dim, dtype=dcm_slice.pixel_array.dtype)

# Iterate over all slices
# Assuming names are stored as '0.dcm', '1.dcm', '2.dcm', etc. 
for name in names:
    idx = int(os.path.splitext(name)[0])
    dcm = pydicom.dcmread(os.path.join(dir, name))
    dcm_data[:,:,idx] = dcm.pixel_array
    
# Uncomment if you want to save it in .MAT format. Because MATLAB's volumeViewer
# requires files in .MAT format.
import scipy.io as sio
sio.savemat('vol3d.mat', {'v': dcm_data}, do_compression=False)    

