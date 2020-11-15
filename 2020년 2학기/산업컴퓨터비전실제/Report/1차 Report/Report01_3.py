import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

#영상 선택
strImage = input('Select image\n -Lena is default\n - F-16 is [F]\n - House is [H] : ')

#선택한 영상 Open
image = cv2.imread(".\lena.png",0).astype(np.float32)/255
if strImage == 'F':
    image = cv2.imread(".\F16.png",0).astype(np.float32)/255
elif strImage == 'H':
    image = cv2.imread(".\House.png",0).astype(np.float32)/255
assert image is not None

#필터 크기와 타입 입력 받기
sz = int(input('Diameter(minimum 5) : '))
if sz < 10:
    sz = 10

strPassType = input('Select filter pass type\n -Low pass is default\n - High pass is [H] : ')

#알고리즘
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0,1])

magnitude = cv2.magnitude(fft_shift[:,:,0], fft_shift[:,:,1])
magnitude = np.log(magnitude)

mask = np.zeros(fft_shift.shape, np.uint8)

centerX = mask.shape[0]//2
centerY = mask.shape[1]//2

powerDist = sz * sz
for yy in range(0, mask.shape[1]):
    for xx in range(0, mask.shape[0]):
        nDist = ( pow(abs(yy-centerY),2) + pow(abs(xx-centerX),2) )
        if nDist < powerDist:
            mask[xx,yy,:] =1

strTitle = 'Low passed image'
if strPassType == 'H':
    mask = 1 - mask
    strTitle = 'High passed image'

fft_shift *= mask

magnitude2 = cv2.magnitude(fft_shift[:,:,0], fft_shift[:,:,1])
magnitude2 = np.log(magnitude2)

fft = np.fft.ifftshift(fft_shift, axes=[0,1])
filtered = cv2.idft(fft, flags = cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)


#Display
plt.figure(figsize=(12,4))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('FFT magnitude')
plt.imshow(magnitude2, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title(strTitle)
plt.imshow(filtered, cmap='gray')
plt.tight_layout()
plt.show()
