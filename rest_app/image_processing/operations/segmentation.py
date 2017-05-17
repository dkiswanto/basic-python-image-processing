import numpy as np
from .grayscale import rgb2gray


def get_threshold(n, mode='fifth-nary'):
    if mode == 'binary':
        if n <= 127:
            return 0
        else:
            return 255
    #  fifth-nary threshold, like in the class
    else:
        if n <= 50:
            return 25
        elif n <= 100:
            return 75
        elif n <= 150:
            return 125
        elif n <= 200:
            return 175
        elif n <= 255:
            return 225


def thresholding(img:np.ndarray, mode='fifth-nary'):
    # Gray image handling
    if len(img.shape) == 3:
        img = rgb2gray(img)

    x,y = img.shape[:2]
    for i in range(x):
        for j in range(y):
            img[i,j] = get_threshold(img[i, j], mode=mode)

    return img


def region_growth():
    pass