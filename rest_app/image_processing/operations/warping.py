import numpy as np


def warp(img: np.ndarray):
    x, y = img.shape[:2]
    warp_level = int((4 / 100) * y)
    # warp_level = 100
    count = 0
    direction = 'left'
    for i in range(x):
        if direction == 'left':
            count += 1
        else:
            count -= 1

        img[i] = np.roll(img[i], count,axis=0)

        if count == warp_level:
            direction = 'right'
        elif count == 0:
            direction = 'left'

        # break
    return img
