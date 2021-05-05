import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression

r= open("CFLU_Data.csv", 'r')
data = csv.reader(r)

header = next(data)
packageID = []
ballID = []
width = []
height = []
width2D = []
for rr in data:
    packageID.append(rr[0])
    ballID.append(rr[1])
    width.append(float(rr[5]))
    height.append(float(rr[3]))
    width2D.append([float(rr[5]), float(rr[5])])

lr = LinearRegression()
lr.fit(width2D, height)
resultLinear = lr.predict(width2D)

ir = IsotonicRegression()
resultIso = ir.fit_transform(width, height)

gapThreshold = 15

wfile = open("CFLU_Data_Regression.csv", 'w', newline ='')
write = csv.writer(wfile)
write.writerow(['PackageID','BallID','Width','Height','Linear','Gap', 'Judge','Isotonic', 'Gap', 'Judge'])
for i in range(0,len(width)):
    gapIso = (float)(height[i]) - resultIso[i]
    gapLinear = (float)(height[i]) - resultLinear[i]
    strResultIso = 'Pass'
    strResultLinear = 'Pass'
    if abs(gapLinear) > gapThreshold:
        strResultLinear = '불량 의심'
    if abs(gapIso) > gapThreshold:
        strResultIso = '불량 의심'

    write.writerow([packageID[i],ballID[i],width[i], height[i], resultLinear[i], gapLinear, strResultLinear, resultIso[i], gapIso, strResultIso])

print("complete! Please Check [CFLU_Data_Regression.csv]")