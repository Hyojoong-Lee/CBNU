import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img1 = cv2.imread(".\AreaLeft.png", cv2.IMREAD_COLOR)
img2 = cv2.imread(".\AreaRight.png", cv2.IMREAD_COLOR)

fast = cv2.FastFeatureDetector_create(60, True, cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
keyPoints1 = fast.detect(img1)
keyPoints2 = fast.detect(img2)

for kp in keyPoints1:
    kp.size = 100 * random.random()
    kp.angle = 360 * random.random()

matches1 = []
for i in range(len(keyPoints1)):
    matches1.append(cv2.DMatch(i, i, 1))

show_img1 = cv2.drawKeypoints(img1, keyPoints1, None, (255, 0, 255))

cv2.imshow('KetPointsLeft', show_img1)
cv2.waitKey()
cv2.destroyAllWindows()

for kp in keyPoints2:
    kp.size = 100 * random.random()
    kp.angle = 360 * random.random()

matches2 = []
for i in range(len(keyPoints2)):
    # matches2.append(matches1)
    matches2.append(cv2.DMatch(i, i, 1))

show_img2 = cv2.drawKeypoints(img2, keyPoints2, None, (255, 0, 255))

cv2.imshow('KetPointsRight', show_img2)
cv2.waitKey()
cv2.destroyAllWindows()

show_img1 = cv2.drawKeypoints(img1, keyPoints1, None, (0, 255, 0),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('KetPointsLeft', show_img1)
cv2.waitKey()
cv2.destroyAllWindows()

show_img2 = cv2.drawKeypoints(img2, keyPoints2, None, (0, 255, 0),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('KetPointsRight', show_img2)
cv2.waitKey()
cv2.destroyAllWindows()

show_img = cv2.drawMatches(img1, keyPoints1, img2, keyPoints2, matches2, None,
                           flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('matches', show_img)
cv2.waitKey()
cv2.destroyAllWindows()
