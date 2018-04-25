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
prevFrameKeypoints = None
prevFrameDescriptors = None
i = 0
while (cap.isOpened()):
	ret, currFrame = cap.read()
	currFrame = cv2.resize(currFrame, (0,0), fx=0.33, fy=0.33); #resize frame to fit on one display

	# sift = cv2.xfeatures2d.SIFT_create(nfeatures=10)
	# currFrameKeypoints, currFrameDescriptors = sift.detectAndCompute(currFrame, None)

	if prevFrame is not None:
		if i == 0:
			i+=1
			continue
		# matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
		# matches = matcher.match(prevFrameDescriptors, currFrameDescriptors)		
		# matches = np.asarray(matches)
	
		# pfkp = np.float32([prevFrameKeypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
		# cfkp = np.float32([currFrameKeypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
		
		# res = cv2.drawMatches(currFrame, currFrameKeypoints, prevFrame, prevFrameKeypoints, matches, None)
		# cv2.imshow('sift features matches', res)

		res = cv2.estimateRigidTransform(currFrame, prevFrame, False)
		dst = cv2.warpAffine(currFrame, res, (np.size(currFrame,1), np.size(currFrame,0)));
		
		# h, status = cv2.findHomography(cfkp, pfkp, cv2.RANSAC)
		# res = cv2.warpPerspective(prevFrame, status, (np.size(currFrame,0), np.size(currFrame,1)))
		cv2.imshow('Stabilized', dst)

	prevFrame = currFrame
	# prevFrameKeypoints = currFrameKeypoints
	# prevFrameDescriptors = currFrameDescriptors
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()