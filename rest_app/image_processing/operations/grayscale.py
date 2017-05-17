import numpy as np


def rgb2gray(image: np.ndarray):

    # if image is RGB
    if len(image.shape) != 2:
        gray_img = np.dot(image, [0.5,0.25,0.25])

        # clip matrix in range 0-255 & set as type=uint8
        np.clip(gray_img, 0, 255, out=gray_img)
        gray_img = gray_img.astype('uint8')
        return gray_img
    # return image directly if image is already Grayscale
    else:
        return image

# array([
#     [[11,12,14], [1,2,3]],
#     [[22,4,10], [41,32,9]],
# ])

# first row, column element = [11,12,14] (R,G,B)
# to converting to greyscale,
# dot product operation (result will only have one value)

# dot product with [1/2,1/4,1/4] for each element (pixel in mage)
