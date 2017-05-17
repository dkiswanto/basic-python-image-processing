import numpy as np

kernel_one = np.ones((3,3))
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]]) # not change anything
kernel_blur = np.ones((3,3)) * 1/9  # oke
gaussian_blur = np.array([[1,2,1],[2,4,2],[1,2,1]]) * 1/16  # oke


def convolution(img:np.ndarray,kernel='one'):
    if kernel == 'one':
        kernel_func = kernel_one
    elif kernel == 'blur':
        kernel_func = kernel_blur
    elif kernel == 'gaussian_blur':
        kernel_func = gaussian_blur
    else:
        kernel_func = kernel_identity

    return filter(img, kernel_func)


def filter(img:np.ndarray, kernel_func):

    # Gray image handling
    if len(img.shape) == 2:
        img = operations(img, kernel_func)

    # RGB image handling
    else:
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]

        img[:, :, 0] = operations(red, kernel_func)
        img[:, :, 1] = operations(green, kernel_func)
        img[:, :, 2] = operations(blue, kernel_func)

    return img


def operations(img:np.ndarray, kernel_func):

    filter_img = np.zeros(img.shape)
    x, y = img.shape

    for i in range(x):
        for j in range(y):

            # first row
            if i == 0:

                # first element
                if j == 0:
                    sub_matrix = img[i:i + 2, j:j + 2].flatten()
                    sub_matrix = np.r_[0, 0, 0, 0, sub_matrix[0:2], 0, sub_matrix[2:4]]

                elif j == y-1:
                    sub_matrix = img[i:i + 2, j - 1:j + 1].flatten()
                    sub_matrix = np.r_[0, 0, 0, sub_matrix[0:2], 0, sub_matrix[2:4],0]
                else:
                    sub_matrix = img[i:i + 2, j - 1:j + 2].flatten()
                    sub_matrix = np.r_[0, 0, 0, sub_matrix[0:3], sub_matrix[3:6]]


            # last row
            elif i == x-1:
                if j == 0:
                    sub_matrix = img[i-1:i+1, j:j + 2].flatten()
                    sub_matrix = np.r_[0, sub_matrix[0:2], 0, sub_matrix[2:4], [0, 0, 0]]

                elif j == y-1:
                    sub_matrix = img[i-1:i+1, j-1:j+1].flatten()
                    sub_matrix = np.r_[sub_matrix[0:2], 0, sub_matrix[2:4], [0,0, 0, 0]]

                else:
                    sub_matrix = img[i-1:i+1, j-1:j + 2].flatten()
                    sub_matrix = np.r_[sub_matrix,[0,0,0]]

            # middle row
            else:
                if j == 0:
                    sub_matrix = img[i-1:i + 2, j:j + 2].flatten()
                    sub_matrix = np.r_[0, sub_matrix[0:2], 0, sub_matrix[2:4],0, sub_matrix[4:6]]

                elif j == y-1:
                    sub_matrix = img[i-1:i + 2, j-1:j + 1].flatten()
                    sub_matrix = np.r_[sub_matrix[0:2], 0, sub_matrix[2:4],0, sub_matrix[4:6],0]

                else:
                    sub_matrix = img[i - 1:i + 2, j - 1:j + 2].flatten()

            filter_img[i, j] = np.dot(sub_matrix, kernel_func.flatten())

    np.clip(filter_img, 0, 255, out=filter_img)
    filter_img = filter_img.astype('uint8')
    return filter_img


# sample matrix
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# traversal element 0
# [[0 1]
#  [3 4]]

# traversal element 1
# [[0 1 2]
#  [3 4 5]]

# traversal element 2
# [[1 2]
#  [4 5]]

# traversal element 3
# [[0 1]
#  [3 4]
#  [6 7]]

# traversal element 4
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# traversal element 5
# [[1 2]
#  [4 5]
#  [7 8]]

# traversal element 6
# [[3 4]
#  [6 7]]

# traversal element 7
# [[3 4 5]
#  [6 7 8]]

# traversal element 8
# [[4 5]
#  [7 8]]
