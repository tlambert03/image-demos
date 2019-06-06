"""
Displays neurons with polygon masks
"""

from skimage.io import imread
import numpy as np
from napari import Viewer
from napari.util import app_context
from skimage.measure import label

mean = imread('data/neurofinder/mean.tif')
polygons = np.load('data/neurofinder/polygons.npy')
mask = imread('data/neurofinder/mask.tif')

with app_context():
    # create an empty viewer
    viewer = Viewer()

    mean_layer = viewer.add_image(mean, name='mean')
    mean_layer.clim = (0.0, 600.0)
    mean_layer.colormap = 'gray'

    shapes_layer = viewer.add_shapes(polygons, shape_type='polygon',
                                     edge_width=0, face_color='green',
                                     opacity=0.5, name='neurons')
    labels = label(mask)
    labels_layer = viewer.add_labels(labels, name='rois')