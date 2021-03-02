from skimage.data import cells3d
import napari

v = napari.view_image(cells3d(), channel_axis=1)
napari.run()
