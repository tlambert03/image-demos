"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

stack = imread('data/mesoscope/anatomical/volume_lowres.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the image
    layer = viewer.add_image(stack.transpose(1, 2, 0), name='stack')
    layer.clim = (0.0, 1500.0)
    layer.colormap = 'gray'
