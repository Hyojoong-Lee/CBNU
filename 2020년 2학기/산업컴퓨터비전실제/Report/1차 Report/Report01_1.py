import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

#영상 선택 및 color Channel 선택
strImage = input('Select image\n -Lena is default\n - F-16 is [F]\n - House is [H] : ')
strChannel = input('Select color channel\n - Red is default\n - Green is [G]\n - Blue is [B] : ')

#선택한 영상 Open
image = cv2.imread(".\lena.png")
if strImage == 'F':
    image = cv2.imread(".\F16.png")
elif strImage == 'H':
    image = cv2.imread(".\House.png")
assert image is not None

#선택한 채널 버퍼 생성
nChannel = 2
if strChannel == 'G':
    nChannel = 1
elif strChannel == 'B':
    nChannel = 0
grayImage = image[:,:,nChannel]

histOriginR, binsOriginR = np.histogram(image[:,:,2], 256, [0,255])
histOriginG, binsOriginG = np.histogram(image[:,:,1], 256, [0,255])
histOriginB, binsOriginB = np.histogram(image[:,:,0], 256, [0,255])

#선택한 채널에 영상 처리 적용 및 기존 영상에 적용
processedImage = image[:,:,[0,1,2]]#원본과 함께 Display하기위해 별도의 Color Buffer 생성
processedGrayImage = cv2.equalizeHist(grayImage)
processedImage[:,:,nChannel] = processedGrayImage

histEqualizedR, binsEqualizedR = np.histogram(processedImage[:,:,2], 256, [0,255])
histEqualizedG, binsEqualizedG = np.histogram(processedImage[:,:,1], 256, [0,255])
histEqualizedB, binsEqualizedB = np.histogram(processedImage[:,:,0], 256, [0,255])

#Display
plt.figure(figsize=[8,8])
plt.subplot(221)
plt.axis('off')
plt.title('Original color')
plt.imshow(image[:,:,[2,1,0]])

plt.subplot(222)
plt.axis('off')
plt.title('Equalized color')
plt.imshow(processedImage[:,:,[2,1,0]])

plt.subplot(223)
plt.title('Original histogram')
plt.fill(histOriginB) #Graph의 색을 맞추기 위해 순서를 변경
plt.fill(histOriginR)
plt.fill(histOriginG)

plt.subplot(224)
plt.title('Equalized histogram')
plt.fill(histEqualizedB)
plt.fill(histEqualizedR)
plt.fill(histEqualizedG)

plt.tight_layout()
plt.show()