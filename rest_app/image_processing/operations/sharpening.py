import numpy as np
from .convolution import filter as convolution_filter


def sharp(img:np.ndarray):
    kernel_sharpening = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # oke
    # using convolution and kernel sharpening
    # bisa dilihat di convolution.txt / convolution.py
    return convolution_filter(img, kernel_sharpening)