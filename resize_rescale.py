import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_resized = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img_resized)
resized_img = rescaleFrame(img_resized)
cv.imshow("Image", resized_img)
cv.waitKey(0)
