"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from skimage.io import imread, imsave
from glob import glob
from napari import Viewer, gui_qt
from os.path import isfile
import warnings

skimage_save_warning = "'%s is a low contrast image' % fname"

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning,
                            message=skimage_save_warning)

base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'
datasets = sorted(glob(base_name))


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the first image
    image = imread(datasets[0] + '/images/image_gray.tif')
    image_layer = viewer.add_image(image, name='0', clim_range=(0, 255))
    image_layer.colormap = 'gray'

    # add the first labels
    if isfile(datasets[0] + '/labels/drawn.tif'):
        labels = imread(datasets[0] + '/labels/drawn.tif')
    else:
        labels = np.zeros(image.shape, dtype=np.int)

    labels_layer = viewer.add_labels(labels, name='labels', opacity=0.5)
    labels_layer.brush_size = 2
    labels_layer.n_dimensional = False

    @viewer.bind_key('s')
    def save(viewer):
        """Save the current annotations
        """
        labels = viewer.layers[1].data.astype(np.uint16)
        name = int(viewer.layers[0].name)
        imsave(datasets[name] + '/labels/drawn.tif', labels, plugin='tifffile',
               photometric='minisblack')
        msg = 'Saving ' + viewer.layers[0].name + ': ' + datasets[name]
        print(msg)
        viewer.status = msg

    @viewer.bind_key('n')
    def next(viewer):
        """Save the current annotation and load the next image and annotation
        """
        save(viewer)
        name = int(viewer.layers[0].name)
        name = name + 1
        if name == len(datasets):
            name = 0

        image = imread(datasets[name] + '/images/image_gray.tif')

        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[0].data = image
        viewer.layers[0].name = str(name)
        viewer.layers[1].data = labels

        msg = 'Loading ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg

    @viewer.bind_key('b')
    def previous(viewer):
        """Save the current annotation and load the previous image and annotation
        """
        save(viewer)
        name = int(viewer.layers[0].name)
        name = name - 1
        if name == -1:
            name = len(datasets)-1

        image = imread(datasets[name] + '/images/image_gray.tif')

        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[0].data = image
        viewer.layers[0].name = str(name)
        viewer.layers[1].data = labels

        msg = 'Loading ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg

    @viewer.bind_key('r')
    def revert(viewer):
        """Loads the last saved annotation
        """
        name = int(viewer.layers[0].name)
        if isfile(datasets[name] + '/labels/drawn.tif'):
            labels = imread(datasets[name] + '/labels/drawn.tif')
        else:
            labels = np.zeros(image.shape, dtype=np.int)

        viewer.layers[1].data = labels

        msg = 'Reverting ' + viewer.layers[0].name
        print(msg)
        viewer.status = msg
