import cv2
import numpy as np
import config
from image_joining.custom_image_joining import stackImages

path = config.GLOBAL_IMG_PATH + "lambo.png"


def empty(a):
    pass


# create track bar
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)

    # convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get the trackbar value
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # masking the image
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)

    # get original image
    img_result = cv2.bitwise_and(img, img, mask=mask)

    #cv2.imshow("Original", img)
    #cv2.imshow("HSV", img_hsv)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Result", img_result)

    # stack image
    img_stack = stackImages(0.6, ([img, img_hsv], [mask, img_result]))
    cv2.imshow("Stack Image", img_stack)

    cv2.waitKey(1)
