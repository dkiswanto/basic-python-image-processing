import numpy as np


def zoom_in(image: np.ndarray):

    # RGB and Greyscale Handler
    try:
        x, y, z = image.shape
        img_zoom = np.zeros((x*2,y*2,z),dtype=np.uint8)
    except:
        x, y = image.shape
        img_zoom = np.zeros((x*2,y*2),dtype=np.uint8)

    # build matrix flip
    for i in range(x):
        for j in range(y):
            m, n = i*2, j*2
            img_zoom[m, n] = image[i,j]
            img_zoom[m+1, n] = image[i, j]
            img_zoom[m, n+1] = image[i, j]
            img_zoom[m+1, n+1] = image[i, j]
    return img_zoom


def zoom_out(image: np.ndarray):
    image = image.astype('uint32')
    try:
        # make container matrix inverse shape
        x, y, z = image.shape
        new_x = int((x/y) * (y//2))
        new_y = y//2
        img_zoom = np.zeros((new_x,new_y, z),dtype=np.uint32)
    except:
        x, y = image.shape
        new_x = int((x/y) * (y//2))
        new_y = y//2
        img_zoom = np.zeros((new_x,new_y),dtype=np.uint32)

    # build matrix flip
    for i in range(new_x):
        for j in range(new_y):
            m, n = i*2, j*2
            img_zoom[i, j] = (image[m,n] + image[m + 1,n] + image[m,n+1] + image[m+1,n+1]) // 4

    np.clip(img_zoom, 0, 255, out=img_zoom)
    img_zoom = img_zoom.astype('uint8')
    return img_zoom
