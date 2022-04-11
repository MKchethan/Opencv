import cv2 as cv
import numpy as np
img = cv.imread("E:\Chethy.jpg")
cv.imshow("Img", img)
blank = np.zeros((800, 800, 3), dtype='uint8')
blank1 = np.zeros((800, 800, 3), dtype='uint8')

cv.rectangle(blank, (250, 350), (500, 500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

cv.line(blank, (250, 350), (380, 230), (0, 255, 0), thickness=3)
cv.imshow('Line', blank)

cv.line(blank, (380, 230), (510, 350), (0, 255, 0), thickness=3)
cv.imshow('Line', blank)

cv.rectangle(blank, (360, 500), (400, 400), (0, 0, 255), thickness=-1)
cv.imshow('Rectangle_', blank)

cv.circle(blank1, (400, 400), 80, (0, 0, 255), thickness=0)
cv.circle(blank1, (360, 360), 10, (0, 0, 255), thickness=0)
cv.circle(blank1, (440, 360), 10, (0, 0, 255), thickness=0)
cv.line(blank1, (390, 440), (410, 440), (0, 255, 0), thickness=3)
cv.imshow("Circle", blank1)

cv.waitKey(0)



