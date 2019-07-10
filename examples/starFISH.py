"""
Displays FISH data, raw and deconvolved, with spots detected using starFISH
"""

from skimage.io import imread
import numpy as np
from napari import Viewer, gui_qt

raw = imread('data/smFISH/raw.tif')
deconvolved = imread('data/smFISH/deconvolved.tif')
spots = np.loadtxt('data/smFISH/spots.csv', delimiter=',')

print(raw.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the raw images
    raw_layer = viewer.add_image(raw, name='images', colormap='gray', clim=(140.0, 1300.0))


    decon_layer = viewer.add_image(deconvolved, name='deconvolved', colormap='gray', clim=(0.0, 0.2))
    decon_layer.visible = False

    spots_layer = viewer.add_points(spots, face_color='red',
                                     edge_color='red', symbol='ring', size=8,
                                     n_dimensional=True, name='spots')
    spots_layer.opacity = 0.5
