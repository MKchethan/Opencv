import cv2 as cv
import numpy as np

img = cv.imread("photos/cats.jpg")
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Green', blank)
#
# # 2. Draw a Rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# # 3. Draw A circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)
#
# # 4. Draw a line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(img, 'Hello, we are a family!!!', (0, 25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 99, 99), 2)
cv.imshow('Text', img)


# colors
# (255, 255, 255) - white
# (0, 0, 0)       - black
# (0, 0, 255)     - Red
# (0, 255, 0)     - Green
# (255, 0, 0)     - Blue
# (255, 255, 0)   - blue shade
# (255, 0, 255)   - Pink shade
# (0, 255, 255)   - Yellow
# (99, 99, 255)   - orange shade
# (99, 99, 99)    - Gray shade

cv.waitKey(0)
