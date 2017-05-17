from matplotlib import pyplot as plt
from rest_app.image_processing.operations import brightness, zoom, flipping, rotate,\
    edge_detection, grayscale, morphology, segmentation, convolution, smoothing, sharpening,\
    warping, histogram, move, open_image

image_dir = 'rest_app/static/images/taeyeon.jpg'
img = open_image.to_matrix(image_dir)
img = grayscale.rgb2gray(img)
# new_image = rotate.rotate90(img)
# new_image = rotate.rotate180(img)
# new_image = rotate.rotate270(img)
# new_image = flipping.flip(img, type='horizontal')
# new_image = flipping.flip(img, type='vertical')
# new_image = zoom.zoom_in(img)
# new_image = zoom.zoom_out(img)
# new_image = move.move(img, 30, direction='down')
# new_image = brightness.brightness(img, 70)
# new_image = brightness.brightness(img, -100)
# new_image = brightness.multiply_brightness(img, 2)
# new_image = brightness.multiply_brightness(img, 10, type='division')
# histogram.split_rgb(img)
# new_image = warping.warp(img)
# new_image = convolution.convolution(img, 'one')   # SLOW
# new_image = convolution.convolution(img, 'blur')
# new_image = convolution.convolution(img, 'gaussian_blur')
# new_image = sharpening.sharp(img)
new_image = edge_detection.edge_detection(img, type=1)
# new_image = smoothing.smooth(img, type='modus') #takes so long in web
# new_image = smoothing.smooth(img, type='mean')
# new_image = smoothing.smooth(img, type='median')
# new_image = segmentation.thresholding(img)
# new_image = segmentation.thresholding(img, mode='binary')
# new_image = morphology.erosion(img)
# new_image = morphology.dilation(img)

# print(new_image)
plt.imshow(new_image, cmap='gray')
plt.show()