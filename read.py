import cv2 as cv

# reading images
# img = cv.imread('photos/cats.jpg')
# cv.imshow('Dog', img)
# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(2) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

