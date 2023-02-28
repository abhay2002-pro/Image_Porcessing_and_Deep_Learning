def my_function(a):
    print("Hello from inside the function ", a)

my_function(1)

#  Default paramter
def my_function(county = "USA"):
    print("Hello from inside the function ", county)

my_function();
my_function("AUS");

# array paramter
def my_function(food):
    for x in food:
        print(x)

my_function(["shahi", "panner"])


from scipy import ndimage
from imageio.v2 import imread, imsave

def rotated(img):
    rotated_image = ndimage.rotate(img, 45);
    imsave('rotated_image.jpeg', rotated_image)

def blurred(img):
    blurred_image = ndimage.gaussian_filter(img, 45);
    imsave('blurred_image.jpeg', blurred_image)

img = imread('temp.jpeg');
rotated(img);
blurred(img);