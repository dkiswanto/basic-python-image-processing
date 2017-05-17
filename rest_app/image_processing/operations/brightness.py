import numpy as np


def brightness(image: np.ndarray, level):
    new_img = np.array(image, dtype=np.uint32) + level
    np.clip(new_img, 0, 255, out=new_img)
    new_img = new_img.astype('uint8')
    return new_img


def multiply_brightness(image: np.ndarray, level, type='multiply'):

    if type == 'multiply':
        new_img = np.array(image, dtype=np.uint32) * level
        np.clip(new_img, 0, 255, out=new_img)
        new_img = new_img.astype('uint8')
        return new_img

    elif type == 'division':
        return image // level   # non float division