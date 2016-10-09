
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import roberts
from skimage.filters import threshold_otsu
from pylab import *

matplotlib.rcParams['font.size'] = 9

#######################
# Función que transforma la imagen inicial en blanco y negro
def rgb2gray (imgArray):
   return np.dot(imgArray[...,:3], [0.299,0.587,0.114])

img = mpimg.imread('/usr/local/lib/python3.5/dist-packages/skimage/data/vallsuau.jpg')
gray = rgb2gray(img)
#
#######################

image = gray
thresh = threshold_otsu(image)
binary = image > thresh

edge_roberts = roberts(binary)


fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(8, 3))
#fig = plt.figure(figsize=(8, 2.5))
#ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
#ax2 = plt.subplot(1, 3, 2)
#ax3 = plt.subplot(1, 3, 3, sharex=ax1, sharey=ax1, adjustable='box-forced')


#ORIGINAL
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')

#HISTOGRAMA
ax2.hist(image)
ax2.set_title('Histogram')
ax2.axvline(thresh, color='r')

#THRESHOLDED
ax3.imshow(binary, cmap=plt.cm.gray)
ax3.set_title('Thresholded')
ax3.axis('off')

#EDGE_ROBERTS
ax4.imshow(edge_roberts, cmap=plt.cm.gray)
ax4.axis('off')
ax4.set_title('Edge Roberts')

im = binary
plt.figure()
contour(im, levels=[0], colors='black', origin='image')

show()

plt.show()















