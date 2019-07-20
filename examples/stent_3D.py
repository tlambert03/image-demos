"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import napari


with np.load('data/vispy_volumes/stent.npz') as array:
    stent = array["data"]

# with np.load('data/vispy_volumes/mri.npz') as array:
#     mri = array["data"]

#vessel_tree = np.load('data/vispy_volumes/vessel_tree_noise.npy')
#vessel_tree = np.load('data/vispy_volumes/skeleton_vessel_tree_noise.npy')


with napari.gui_qt():
    viewer = napari.Viewer()

    # add the volume
    viewer.add_volume(stent, name='stent')
