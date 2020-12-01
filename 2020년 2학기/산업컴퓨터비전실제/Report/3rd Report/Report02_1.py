import cv2
import numpy as np
import matplotlib.pyplot as plt

fileName = []
fileName.append('./boat1.jpg')
fileName.append('./budapest1.jpg')
fileName.append('./newspaper1.jpg')
fileName.append('./s1.jpg')

for i in range(len(fileName)):
    image = cv2.imread(fileName[i], cv2.IMREAD_COLOR)

    #Canny Edge
    show_CanntEdgeImg = cv2.Canny(image, 200,100)

    #Harris Corner
    corners = cv2.cornerHarris(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    show_HarrisImg = np.copy(image)
    show_HarrisImg [corners > 0.1 * corners.max()] = [0,0,255]

    # Display
    plt.figure(figsize=[17, 6])
    plt.subplot(131)
    plt.axis('off')
    plt.title('Original color')
    plt.imshow(image[:, :, [2, 1, 0]])

    plt.subplot(132)
    plt.axis('off')
    plt.title('Canny Edge')
    plt.imshow(show_CanntEdgeImg, cmap='gray')

    plt.subplot(133)
    plt.axis('off')
    plt.title('Harris Corner')
    plt.imshow(show_HarrisImg[:, :, [2, 1, 0]])

    plt.tight_layout()
    plt.show()

