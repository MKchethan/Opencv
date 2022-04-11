import cv2 as cv

chethy = cv.imread("photos/Chethy.jpg")
img = cv.imread("photos/cat.jpg")
cv.imshow("Image", img)

# gray
# gray = cv.cvtColor(chethy, cv.COLOR_BGRA2GRAY)
# cv.imshow("Gray", gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # numbers should be odd more the no more blur it is
cv.imshow('Blur', blur)
#
# # Edge Cascade
canny1 = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny1)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)
#
# # Dilating the image
dilated = cv.dilate(canny1, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)
#
# # Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)
#
# # Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
#
# # Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
