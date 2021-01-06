import cv2

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture("D:\\ml-datasets\\open-cv-dataset\\video\\sample.mpg")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frame_width, frame_height))
    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
