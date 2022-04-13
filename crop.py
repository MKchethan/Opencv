import cv2 as cv
import numpy as np

img = cv.imread("photos/cards.jpg")

width, height = 200, 300
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

croppedImg = img[219:450, 111:352]

cv.imshow("Image", img)
cv.imshow("Output_image", imgOutput)
cv.imshow("Cropped_image", croppedImg)

cv.waitKey(0)
