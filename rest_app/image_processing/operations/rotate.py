import numpy as np


def rotate90(image : np.ndarray):

    # RGB and Greyscale Handler
    try:
        x, y, z = image.shape
        img_rotate = np.zeros((y,x,z),dtype=np.uint8)
    except:
        x, y = image.shape
        img_rotate = np.zeros((y,x),dtype=np.uint8)

    # build matrix rotate
    for i in range(x):
        for j in range(y):
            img_rotate[j, x-i-1] = image[i,j]
    return img_rotate

# array([[1, 2, 3],
       # [4, 5, 6]])

# array([[0, 0],
       # [0, 0],
       # [0, 0]], dtype=uint8)

# array([[4, 1],
       # [5, 2],
       # [6, 3]], dtype=uint8)


def rotate180(image: np.ndarray):
    x, y = image.shape[:2]
    img_rotate = np.zeros(image.shape,dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            img_rotate[x-i-1, y-j-1] = image[i,j]
    return img_rotate

# array([[1, 2, 3],
       # [4, 5, 6]])

# array([[6, 5, 4],
       # [3, 2, 1]])


def rotate270(image: np.ndarray):
    return rotate90(rotate180(image))
