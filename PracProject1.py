import cv2 as cv
import numpy as np

img1 = cv.imread("photos/lambo.png")
img2 = cv.imread("photos/green.jpg")

myColors = [[57, 76, 0, 100, 255, 255],[5, 107, 0, 19, 255, 255],
            ]


def findColor(img, myColors):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        cv.imshow(str(color[0]), mask)


findColor(img1, myColors)
findColor(img2, myColors)
cv.waitKey(0)



