from scipy import misc


def to_matrix(dir):
    image_load = misc.imread(dir, mode='RGBA')

    # get array opacity image
    alpha = image_load[:, :, 3]

    # mask == numpy array boolean
    mask = (alpha == 0)

    # replace rgb with white, if opacity == 0 (transparent)
    image_load[:, :, :3][mask] = [255, 255, 255]
    return image_load[:, :, :3]

