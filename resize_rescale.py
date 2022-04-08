# pylint:disable=no-member
import cv2 as cv


# def changeRes(width, height):
#     # can be used only for Live video
#     capture.set(3, width)
#     capture.set(4, height)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading images
# img_resized = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img_resized)
# resized_img = rescaleFrame(img_resized)
# cv.imshow("Image", resized_img)
# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame_ = capture.read()

    frame_resized = rescaleFrame(frame_)

    cv.imshow('Video', frame_)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


