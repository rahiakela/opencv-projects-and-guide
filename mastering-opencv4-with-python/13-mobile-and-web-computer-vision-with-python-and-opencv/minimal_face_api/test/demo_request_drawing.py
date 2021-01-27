import numpy as np
import requests
import cv2
from matplotlib import pyplot as plt


def show_img_with_matplotlib(color, title, pos):
    """Shows an image using matplotlib capabilities"""

    RGB = color[:, :, ::-1]

    ax = plt.subplot(1, 1, pos)
    plt.imshow(RGB)
    plt.title(title)
    plt.axis("off")


FACE_DETECTION_REST_API_URL = "http://localhost:5000/detect"
IMAGE_PATH = "images/test_face_processing.jpg"

# Load the image and construct the payload
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

response = requests.post(FACE_DETECTION_REST_API_URL, files=payload)
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))

# Get JSON data from the response and get 'result'
json_data = response.json()
result = json_data["result"]

# Convert the loaded image to the OpenCV format
image_array = np.asarray(bytearray(image), dtype=np.uint8)
img_opencv = cv2.imdecode(image_array, -1)

# Draw faces in the OpenCV image
for face in result:
    left, top, right, bottom = face["box"]
    # To draw a rectangle, you need top-left corner and bottom-right corner of rectangle
    cv2.rectangle(img_opencv, (left, top), (right, bottom), (0, 255, 255), 2)
    # Draw top-left corner and bottom-right corner (checking)
    cv2.circle(img_opencv, (left, top), 5, (0, 0, 255), -1)
    cv2.circle(img_opencv, (right, bottom), 5, (255, 0, 0), -1)

# Create the dimensions of the figure and set title
fig = plt.figure(figsize=(8, 6))
plt.suptitle("Using face API", fontsize=14, fontweight="bold")
fig.patch.set_facecolor("silver")

# Show the output image
show_img_with_matplotlib(img_opencv, "face detection", 1)

# Show the Figure
plt.show()