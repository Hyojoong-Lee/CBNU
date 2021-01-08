import cv2
import numpy as np
import glob
import time

imagesPath = []
imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_1frame_*'))))
imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_2frame_*'))))
#imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_3frame_*'))))
imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_4frame_*'))))
#imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_5frame_*'))))
#imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_6frame_*'))))
imagesPath.append(list(sorted(glob.glob('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/Sample/stitchRaw_7frame_*'))))

resultImagesPath = []
resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage01.bmp')
resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage02.bmp')
#resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage03.bmp')
resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage04.bmp')
#resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage05.bmp')
#resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage06.bmp')
resultImagesPath.append('D:/Depot/Depot_GraduateSchool/IndustrialVision/Final_Report/ResultImage07.bmp')

stitcher = cv2.createStitcher()

for i in range(len(imagesPath)):
    images = []
    for img_path in range(len(imagesPath[i])):
        images.append(cv2.imread(imagesPath[i][img_path], cv2.IMREAD_COLOR))

    startTime = time.time()

    ret, pano = stitcher.stitch(images)

    totalTime = time.time() - startTime
    print("time : ", totalTime)

    images.clear()

    if ret == cv2.STITCHER_OK:
        cv2.imwrite(resultImagesPath[i], pano)
        sizeX = pano.shape[1]
        scale = 1200 / sizeX
        pano = cv2.resize(pano, dsize=(0,0), fx=scale, fy=scale)
        cv2.imshow(resultImagesPath[i], pano)
        cv2.waitKey()
        cv2.destroyAllWindows()

    else:
        print('error during stitching')
