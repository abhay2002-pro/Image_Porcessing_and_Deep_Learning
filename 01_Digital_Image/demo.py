import cv2
from skimage.filters import sobel
# 1 -> colored image, 0 -> black and white
img = cv2.imread("temp.jpeg", 1);
img2 = sobel(img);

cv2.imshow("pic", img);
cv2.imshow("pic", img2);
print(img.shape);

# minimum wait time before closing the image tab after pressing key
cv2.waitKey(0)
cv2.destroyAllWindows()
