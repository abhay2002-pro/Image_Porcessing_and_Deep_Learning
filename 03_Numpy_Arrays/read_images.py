import numpy as np
from imageio.v2 import imread, imsave

img = imread('temp.jpeg')
# print(img)
print(type(img))
print(img.shape, img.dtype)

# Only blue will be there
img_tinted = img * [0., 0., 1.]
imsave('tinted.jpeg',img_tinted);