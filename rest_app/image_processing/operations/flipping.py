import numpy as np


def flip(image: np.ndarray, type="horizontal"):
    # get an unpack shape & create container
    x, y = image.shape[:2]
    img_rotate = np.zeros(image.shape,dtype=np.uint8)

    # build matrix flip
    for i in range(x):
        for j in range(y):
            if type == 'horizontal':
                img_rotate[i, y-j-1] = image[i,j]
            elif type == 'vertical':
                img_rotate[x-i-1, j] = image[i,j]
    return img_rotate

# Horizontal Sample
# array([[1, 2, 3],
       # [4, 5, 6]])
# array([[3, 2, 1],
       # [6, 5, 4]])

# Vertical Sample
# array([[1, 2, 3],
       # [4, 5, 6]])
# array([[4, 5, 6],
       # [1, 2, 3]])
