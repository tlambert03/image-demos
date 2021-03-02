import numpy as np
import napari

large = False
large = "_large" if large else ""

base = "data/microglia/SingleCoord/target/reconstructed_birefring_microglia_single_{}{}.npy"

azimuth = np.load(base.format("azimuth", large)) - np.pi / 2
pol = np.load(base.format("polarization", large))
trans = np.load(base.format("I_trans", large))
retard = np.load(base.format("retard", large))

complex_image = np.clip(pol -0.97, 0, 1) * np.exp(1j * azimuth)

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(complex_image)
    # viewer.add_image(pol, name="pol")
    # viewer.add_image(azimuth, name="azimuth")
