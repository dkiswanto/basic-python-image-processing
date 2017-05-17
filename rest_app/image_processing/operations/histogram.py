import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from .grayscale import rgb2gray


def split_rgb(image: np.ndarray):

    # Gray image handling
    if len(image.shape) == 2:
        gray_freq = [0] * 256
        for i in image.flatten():
            gray_freq[i] += 1

        f, axarr = plt.subplots(1)
        y = range(256)
        axarr.bar(y, gray_freq, width=2, facecolor='grey')
        axarr.set_xlim((0,255))

        return plt

    # RGB image handling
    else:

        red = image[:,:,0]
        green = image[:,:,1]
        blue = image[:,:,2]
        gray = rgb2gray(image)
        # print(gray.shape)

        # build data, by get each pixel color by frequency
        red_freq, green_freq, blue_freq, gray_freq = [0] * 256, [0] * 256, [0] * 256, [0] * 256
        for i,j,k,l in zip(red.flatten(), green.flatten(), blue.flatten(), gray.flatten()):
            red_freq[i] += 1
            green_freq[j] += 1
            blue_freq[k] += 1
            gray_freq[l] += 1

        # print(red_freq)
        # create bar plot
        f, axarr = plt.subplots(4)
        colors = ('red', 'green', 'blue', 'grey')
        datas = (red_freq, green_freq, blue_freq, gray_freq)
        subplots = range(4)
        y = range(256)
        for data, i, color in zip(datas,subplots, colors):
            axarr[i].bar(y,data, width=2, facecolor=color)
            axarr[i].set_xlim((0,255))

        # plt.show()
        f.subplots_adjust(hspace=0.3)
        return plt

