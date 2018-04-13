import argparse
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to the input video")
args = vars(ap.parse_args())

print args

cap = cv2.VideoCapture("dataset/" + args["video"])

# for i in range(0, cap.get(CV_CAP_PROP_FRAME_COUNT)-1):
while (cap.isOpened()):
	ret, frame = cap.read()
	# ret, frame1 = cap.get(i)
	# w1, h1 = cv2.GetSize(frame1)
	# ret, frame2 = cap.get(i+1)
	# w2, h2 = cv2.GetSize(frame2)

	# TODO: get original video and stablized imgage to appear side by side
	# canvas = np.zeros(w1, h1*2+10)
	# canvas[0,h1] = frame1
	# canvas[h1+10, ]

	frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5);
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	dst = cv2.cornerHarris(gray,2,3,0.04)

	
	frame[dst>0.01*dst.max()]=[0,0,255]
	cv2.imshow('dst', frame)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break


