# Referenced from https://www.pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
# Image generated from https://fodi.github.io/arucosheetgen/

from imutils.video import VideoStream
import cv2
import imutils
import sys
import time

image_path = "./images/aruco_1.png"
aruco_type = "DICT_4X4_50"

# define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000
}

# load the input image from disk and resize it
print("[INFO] loading image...")
image = cv2.imread(image_path)
image = imutils.resize(image, width=600)
# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(aruco_type, None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		aruco_type))
	sys.exit(0)
# load the ArUCo dictionary, grab the ArUCo parameters, and detect
# the markers
print("[INFO] detecting '{}' tags...".format(aruco_type))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[aruco_type])
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,
	parameters=arucoParams)

print(ids)