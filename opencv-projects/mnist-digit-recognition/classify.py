import joblib
from hog import HOG
import dataset
import mahotas
import cv2
import config


# load the trained model
model = joblib.load("models/svm.cpickle")

# instantiates HOG descriptor
hog = HOG(orientations=18, pixels_per_cell=(10, 10), cells_per_block=(1, 1), transform=True)

# classify the digits in the image
image = cv2.imread(config.GLOBAL_IMG_PATH + "cellphone.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply Gaussian blurring
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# apply Canny edge detector
edged = cv2.Canny(blurred, 30, 150)

# finds contours in the edged image and sorts them from left to right
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key=lambda x: x[1])


