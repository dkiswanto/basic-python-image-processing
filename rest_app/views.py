from PIL import Image
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scipy import misc
import numpy as np

from rest_app.image_processing.operations import brightness, zoom, flipping, rotate,\
    edge_detection, grayscale, morphology, segmentation, convolution, smoothing, sharpening,\
    warping, histogram, move, open_image


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def transform(request):
    if request.method == "POST":

        # validation image request
        image_request = request.FILES.get('image')
        operation = request.POST.get('operation')
        greyscale_mode = request.POST.get('greyscale')
        if image_request is None or operation is None or greyscale_mode is None :
            return HttpResponseForbidden()

        # convert image to matrix
        image_matrix = open_image.to_matrix(image_request)

        # greyscale_mode condition:
        if greyscale_mode == 'true':
            print('Greyscale Mode On')
            image_matrix = grayscale.rgb2gray(image_matrix)

        # process image
        image_matrix = image_processing(image_matrix, operation)

        response = HttpResponse(content_type="image/png")

        # condition save image (picture or histogram)
        if type(image_matrix) == np.ndarray:

            image_data = misc.toimage(image_matrix)

            # background = Image.new("RGB", image_data.size, (255, 255, 255))
            # background.paste(image_data, mask=image_data.split())  # 3 is the alpha channel

            image_data.save(response, "PNG")
        else:
            image_matrix.savefig(response)

        # return image as response
        return response
    else:
        return HttpResponseForbidden()


def image_processing(image_matrix, operation):
    if operation == 'rotate-90':
        return rotate.rotate90(image_matrix)
    elif operation == 'rotate-180':
        return rotate.rotate180(image_matrix)
    elif operation == 'rotate-270':
        return rotate.rotate270(image_matrix)
    elif operation == 'flip-h':
        return flipping.flip(image_matrix, type='horizontal')
    elif operation == 'flip-v':
        return flipping.flip(image_matrix, type='vertical')
    elif operation == 'zoom-in':
        return zoom.zoom_in(image_matrix)
    elif operation == 'zoom-out':
        return zoom.zoom_out(image_matrix)
    elif operation == 'bright+10':
        return brightness.brightness(image_matrix, 10)
    elif operation == 'bright-10':
        return brightness.brightness(image_matrix, -10)
    elif operation == 'brightX2':
        return brightness.multiply_brightness(image_matrix, 2)
    elif operation == 'bright/2':
        return brightness.multiply_brightness(image_matrix, 2, type='division')
    elif operation == 'smooth-modus':
        return smoothing.smooth(image_matrix, type='modus')
    elif operation == 'smooth-mean':
        return smoothing.smooth(image_matrix, type='mean')
    elif operation == 'smooth-median':
        return smoothing.smooth(image_matrix, type='median')
    elif operation == 'sharpening':
        return sharpening.sharp(image_matrix)
    elif operation == 'edge-detect':
        return edge_detection.edge_detection(image_matrix, type=1)
    elif operation == 'greyscale':
        return grayscale.rgb2gray(image_matrix)
    elif operation == 'move-up':
        return move.move(image_matrix, 10, direction='up')
    elif operation == 'move-down':
        return move.move(image_matrix, 10, direction='down')
    elif operation == 'move-left':
        return move.move(image_matrix, 10, direction='left')
    elif operation == 'move-right':
        return move.move(image_matrix, 10, direction='right')
    elif operation == 'warping':
        return warping.warp(image_matrix)
    elif operation == 'histogram':
        return histogram.split_rgb(image_matrix)
    elif operation == 'conv-one':
        return convolution.convolution(image_matrix, 'one')
    elif operation == 'conv-blur':
        return convolution.convolution(image_matrix, 'blur')
    elif operation == 'conv-gaussian':
        return convolution.convolution(image_matrix, 'gaussian_blur')
    elif operation == 'segmentation':
        return segmentation.thresholding(image_matrix)
    elif operation == 'segmentation-binary':
        return segmentation.thresholding(image_matrix, mode='binary')
    elif operation == 'erosion':
        return morphology.erosion(image_matrix)
    elif operation == 'dilation':
        return morphology.dilation(image_matrix)

    else:
        return image_matrix
