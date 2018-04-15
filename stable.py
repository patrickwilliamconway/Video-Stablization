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
prevFrame = None

while (cap.isOpened()):
	ret, frame = cap.read()


	if prevFrame is not None:
		frame = cv2.resize(frame, (0,0), fx=0.3, fy=0.3); #resize frame to fit on one display
		uneditedFrame = np.copy(frame) #keep unedited reference for side by side comparison
		
		# Harris corner detection on frame for keypoints
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		dst = cv2.cornerHarris(gray,2,3,0.04)
		frame[dst>0.01*dst.max()]=[0,0,255]

		# TODO: Combine these into one canvas
		# rows = np.size(frame, 0)
		# cols = np.size(frame, 1)
		# canvas = np.zeros((rows, cols*2+10, 3), dtype=int)
		# canvas[:, range(0, cols)] = uneditedFrame[: , range(0, cols)]
		# canvas[:, range(cols+10, cols*2+10)] = frame[: , range(0, cols)]
		# cv2.imshow('Unstabilized on left, Stabilized on right', canvas)

		cv2.imshow('frame', frame)
		cv2.imshow('uneditedFrame', uneditedFrame)

	prevFrame = frame
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()