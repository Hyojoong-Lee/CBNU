import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

#영상 선택
strImage = input('Select image\n - Lena is default\n - F-16 is [F]\n - House is [H] : ')

#선택한 영상 Open
image = cv2.imread(".\lena.png").astype(np.float32)/255
if strImage == 'F':
    image = cv2.imread(".\F16.png").astype(np.float32)/255
elif strImage == 'H':
    image = cv2.imread(".\House.png").astype(np.float32)/255
assert image is not None

#Noise 추가
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0,1)

#각 값을 입력 받아 필터링
diameter = int(input('Diameter(Default -1) : '))
sigmaColor = float(input('sigmaColor(Default 0.3) : '))
sigmaSpace = int(input('sigmaSpace(Default 10) : '))
bolat = cv2.bilateralFilter(noised, diameter, sigmaColor, sigmaSpace)

#Display
plt.figure(figsize=(12,4))
plt.subplot(131)
plt.axis('off')
plt.title('Original')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(132)
plt.axis('off')
plt.title('Noised')
plt.imshow(noised[:,:,[2,1,0]])
plt.subplot(133)
plt.axis('off')
plt.title('bilateralFilter')
plt.imshow(bolat[:,:,[2,1,0]])
plt.tight_layout()
plt.show()
