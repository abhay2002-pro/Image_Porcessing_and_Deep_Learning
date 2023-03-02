#  Majorly four libraries are there to read images
#  1) Pillow  2) matplotlib   3) scikit-learn  4) open cv

#  ========= Pillow ============
from PIL import Image
import numpy as np

img = Image.open("temp.jpeg");
# not a numpy array
print(type(img));

# img.show();
print(img.format);

# coversion to numpy array
img1 = np.asarray(img);
print(type(img1));

#  ========= Matplotlib ============
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

img = mpimg.imread("temp.jpeg");
print(img);
# imported as a numpy array
print(type(img));
print(img.shape);
# plt.imshow(img);

#  ========= Scikit ============

from skimage import io, img_as_float
from matplotlib import pyplot as plt

image = io.imread("temp.jpeg")
print(type(image))
# plt.imshow(image);

# will scale the image to pixel/max_pixel -> all numbers will be from 0 to 1
image_float = img_as_float(image);
print(image_float)

#  ========= openCV ============
import cv2
from matplotlib import pyplot as plt

#  0 for grayscale image
grey_img = cv2.imread("temp.jpeg", 0)
cv2.imshow("grey image" ,grey_img);
cv2.waitkey(0)
cv2.destroyAllWindows();