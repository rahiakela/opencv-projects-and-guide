import cv2
import numpy as np

img_width = 640
img_height = 480

cap = cv2.VideoCapture(0)
cap.set(3, img_width)
cap.set(4, img_height)
cap.set(10, 150)


def preprocessing(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blurred, 200, 200)
    kernel = np.ones((5, 5))
    img_dilated = cv2.dilate(img_canny, kernel, iterations=2)
    img_thres = cv2.erode(img_dilated, kernel, iterations=2)

    return img_thres


def get_contours(img):
    biggest = np.array([])
    max_area = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest

def get_warp():
    pass

while True:
    success, img = cap.read()
    img = cv2.resize(img, (img_width, img_height))
    img_contour = img.copy()
    img_thres = preprocessing(img)
    biggest = get_contours(img_thres)
    cv2.imshow("Result", img_thres)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
