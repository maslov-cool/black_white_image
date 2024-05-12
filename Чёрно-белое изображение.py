import numpy
from PIL import Image


def bw_convert():
    im = Image.open('image.jpg')
    x, y = im.size
    Image.fromarray(numpy.uint8(numpy.repeat(numpy.round(numpy.sum(numpy.asarray(im) *
                                                                   numpy.array([[[0.2989, 0.5870, 0.1140]]]), axis=2)),
                                             3).reshape(y, x, 3))).save('res.jpg')


bw_convert()
