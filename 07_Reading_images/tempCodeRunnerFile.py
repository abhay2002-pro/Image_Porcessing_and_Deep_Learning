import cv2
from matplotlib import pyplot as plt

#  0 for grayscale image
grey_img = cv2.imread("temp.jpeg", 0)
cv2.imshow("grey image" ,grey_img);
cv2.waitkey(0)
cv2.destroyAllWindows();