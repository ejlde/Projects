import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img_dark = cv2.imread('Dark View 3_9 0d5ms.tif',0) # 0 = grayscale
img = cv2.imread('Direct View 3_9 0d05ms.tif',0)
shape = img.shape
#print(shape)
#print(img[5][5])
intensities = np.zeros((1,2048,2048))
print(intensities)


for i in range(0,2047): 
    for j in range(0,2047):
        intensities[i][j] = img[i][j]

# img_new = Image.open("Direct View 3_9 0d05ms.tif")
# px = img_new.load()
# print(px[4,4])
  
# alternative way to find histogram of an image
# plt.hist(img.ravel(),256,[0,256])
# plt.title('Intensity Histogram Direct View 5ms')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Number of Pixels')
# plt.show()

"""
Bias = 4 bins
"""
