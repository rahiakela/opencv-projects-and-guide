import requests

FACE_DETECTION_REST_API_URL = "http://localhost:5000/detect"
FACE_DETECTION_REST_API_URL_WRONG = "http://localhost:5000/process"
IMAGE_PATH = "test_face_processing.jpg"
URL_IMAGE = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"

# Submit the GET request
response = requests.get(FACE_DETECTION_REST_API_URL_WRONG)
# See the response
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.text))

# Submit the GET request
payload = {"url": URL_IMAGE}
response = requests.get(FACE_DETECTION_REST_API_URL, params=payload)
# See the response
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))
