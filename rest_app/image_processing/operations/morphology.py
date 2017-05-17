import numpy as np


def erosion(img:np.ndarray):
    # Gray image handling
    if len(img.shape) == 2:
        img = operations(img, type='erosion')

    # RGB image handling
    else:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]

        img[:, :, 0] = operations(red, type='erosion')
        img[:, :, 1] = operations(green, type='erosion')
        img[:, :, 2] = operations(blue, type='erosion')

    return img


def dilation(img:np.ndarray):
    # Gray image handling
    if len(img.shape) == 2:
        img = operations(img)

    # RGB image handling
    else:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]

        img[:, :, 0] = operations(red)
        img[:, :, 1] = operations(green)
        img[:, :, 2] = operations(blue)

    return img


def operations(img:np.ndarray, type='dilation'):

    filter_img = np.zeros(img.shape, dtype=np.uint8)
    x, y = img.shape

    for i in range(x):
        for j in range(y):
            # first row
            if i == 0:
                # first element
                if j == 0:
                    sub_matrix = img[i:i + 2, j:j + 2]
                elif j == y-1:
                    sub_matrix = img[i:i + 2, j - 1:j + 1]
                else:
                    sub_matrix = img[i:i + 2, j - 1:j + 2]
            # last row
            elif i == x-1:
                if j == 0:
                    sub_matrix = img[i-1:i+1, j:j + 2]
                elif j == y-1:
                    sub_matrix = img[i-1:i+1, j-1:j+1]
                else:
                    sub_matrix = img[i-1:i+1, j-1:j + 2]
            # middle row
            else:
                if j == 0:
                    sub_matrix = img[i-1:i + 2, j:j + 2]
                elif j == y-1:
                    sub_matrix = img[i-1:i + 2, j-1:j + 1]
                else:
                    sub_matrix = img[i - 1:i + 2, j - 1:j + 2]

            if type == 'dilation':
                filter_img[i, j] = np.max(sub_matrix)
            else:
                filter_img[i, j] = np.min(sub_matrix)

    return filter_img


