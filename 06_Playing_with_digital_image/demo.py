from skimage import io
import numpy as np
from matplotlib import pyplot as plt

# uint - 0 to 255
my_image = io.imread('temp.jpeg')
plt.imshow(my_image)
print(my_image.min(), my_image.max());

from skimage import img_as_float
# float - o to 1
my_float_image = img_as_float(my_image)
plt.imshow(my_float_image)
print(my_float_image.min(), my_float_image.max());