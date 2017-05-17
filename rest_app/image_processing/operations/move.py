import numpy as np


def move(image:np.ndarray, percentage, direction='right'):
    x,y = image.shape[:2]
    img_mov = np.zeros(image.shape, dtype=np.uint8)

    if direction == "up" or direction == "down":
        cut_dim = int(x * percentage / 100)  # round division (non float)
    else:
        cut_dim = int(y * percentage / 100)  # round division (non float)

    if direction == "left":
        img_mov[:, :y - cut_dim] = image[:, cut_dim:]

    elif direction == "right":
        img_mov[:, cut_dim:] = image[:, :y - cut_dim]

    elif direction == "up":
        img_mov[:x-cut_dim, :] = image[cut_dim:, :]

    elif direction== "down":
        img_mov[cut_dim:, :] = image[:x-cut_dim, :]

    return img_mov

    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]], dtype=uint8)
    #
    # array([[2, 3],
    #        [5, 6],
    #        [8, 9]], dtype=uint8)
    #
    # array([[0, 0, 0],
    #        [0, 0, 0],
    #        [0, 0, 0]], dtype=uint8)
    #
    # array([[0, 2, 3],
    #        [0, 5, 6],
    #        [0, 8, 9]], dtype=uint8)
