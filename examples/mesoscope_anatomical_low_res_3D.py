"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import Viewer, gui_qt

stack = imread('data/mesoscope/anatomical/volume_lowres.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    layer = viewer.add_image(stack, name='stack', contrast_limits=(0.0, 1500.0), colormap='gray')
