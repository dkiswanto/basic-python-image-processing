import numpy as np


def smooth(img:np.ndarray, type='mean'):
    # import time
    # start_time = time.time()

    # Gray image handling
    if len(img.shape) == 2:
        if type == 'mean':
            img = filter(img, mode='mean')
        elif type == 'median':
            img = filter(img, mode='median')
        elif  type == 'modus':
            img = filter(img, mode='modus')

    # RGB image handling
    else:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]

        if type == 'mean':
            img[:, :, 0] = filter(red, mode='mean')
            img[:, :, 1] = filter(green, mode='mean')
            img[:, :, 2] = filter(blue, mode='mean')
        elif type == 'median':
            img[:, :, 0] = filter(red, mode='median')
            img[:, :, 1] = filter(green, mode='median')
            img[:, :, 2] = filter(blue, mode='median')
        elif type == 'modus':
            img[:, :, 0] = filter(red, mode='modus')
            img[:, :, 1] = filter(green, mode='modus')
            img[:, :, 2] = filter(blue, mode='modus')

    # print("--- %s seconds ---" % (time.time() - start_time))
    return img


def filter(img:np.ndarray, mode='mean'):

    filter_img = np.zeros(img.shape)
    x, y = img.shape

    for i in range(x):
        for j in range(y):

            # first row
            if i == 0:
                # first element
                if j == 0:
                    if mode == 'mean':
                        sub_matrix = img[i:i + 2, j:j + 2]
                    else:
                        sub_matrix = img[i:i + 2, j:j + 2].flatten()
                        sub_matrix = np.r_[0, 0, 0, 0, sub_matrix[0:2], 0, sub_matrix[2:4]]
                elif j == y-1:
                    if mode == 'mean':
                        sub_matrix = img[i:i + 2, j - 1:j + 1]
                    else:
                        sub_matrix = img[i:i + 2, j - 1:j + 1].flatten()
                        sub_matrix = np.r_[0, 0, 0, sub_matrix[0:2], 0, sub_matrix[2:4],0]
                else:
                    if mode == 'mean':
                        sub_matrix = img[i:i + 2, j - 1:j + 2]
                    else:
                        sub_matrix = img[i:i + 2, j - 1:j + 2].flatten()
                        sub_matrix = np.r_[0, 0, 0, sub_matrix[0:3], sub_matrix[3:6]]
            # last row
            elif i == x-1:
                if j == 0:
                    if mode == 'mean':
                        sub_matrix = img[i-1:i+1, j:j + 2]
                    else:
                        sub_matrix = img[i-1:i+1, j:j + 2].flatten()
                        sub_matrix = np.r_[0, sub_matrix[0:2], 0, sub_matrix[2:4], [0, 0, 0]]
                elif j == y-1:
                    if mode == 'mean':
                        sub_matrix = img[i - 1:i + 1, j - 1:j + 1]
                    else:
                        sub_matrix = img[i-1:i+1, j-1:j+1].flatten()
                        sub_matrix = np.r_[sub_matrix[0:2], 0, sub_matrix[2:4], [0,0, 0, 0]]
                else:
                    if mode == 'mean':
                        sub_matrix = img[i - 1:i + 1, j - 1:j + 2]
                    else:
                        sub_matrix = img[i-1:i+1, j-1:j + 2].flatten()
                        sub_matrix = np.r_[sub_matrix,[0,0,0]]
            # middle row
            else:
                if j == 0:
                    if mode == 'mean':
                        sub_matrix = img[i - 1:i + 2, j:j + 2]
                    else:
                        sub_matrix = img[i-1:i + 2, j:j + 2].flatten()
                        sub_matrix = np.r_[0, sub_matrix[0:2], 0, sub_matrix[2:4],0, sub_matrix[4:6]]
                elif j == y-1:
                    if mode == 'mean':
                        sub_matrix = img[i - 1:i + 2, j - 1:j + 1]
                    else:
                        sub_matrix = img[i-1:i + 2, j-1:j + 1].flatten()
                        sub_matrix = np.r_[sub_matrix[0:2], 0, sub_matrix[2:4],0, sub_matrix[4:6],0]
                else:
                    if mode == 'mean':
                        sub_matrix = img[i - 1:i + 2, j - 1:j + 2]
                    else:
                        sub_matrix = img[i - 1:i + 2, j - 1:j + 2].flatten()

            if mode == 'mean':
                filter_img[i, j] = np.sum(sub_matrix) / 9
            elif mode == 'modus':
                filter_img[i, j] = np.bincount(sub_matrix).argmax()
            elif mode == 'median':
                filter_img[i, j] = np.median(sub_matrix)

    np.clip(filter_img, 0, 255, out=filter_img)
    filter_img = filter_img.astype('uint8')
    return filter_img
