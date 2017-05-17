import numpy as np
from .convolution import filter as convolution_filter


def edge_detection(img:np.array, type=1):

    if type == 1:
        kernel_edge_detection = np.array([[0,1,0],[1,-4,1],[0,1,0]]) # ?
    else:
        kernel_edge_detection = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])  #


    return convolution_filter(img, kernel_edge_detection)
