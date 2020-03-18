# Smoothing an image 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread()
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5), np.float32)/25

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
dest = cv2.filter2D(img,-1,kernel)
bi = cv2.bilateralFilter(img,9,75,75)
med = cv2.medianBlur(img, 5)
 
titles=['image','2dconv','blur','gblur','bilateral','medianblur']
images=[img, dest, blur, gblur, bi, med]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
