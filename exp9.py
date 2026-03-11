import cv2
import numpy as np

# Open webcam
video = cv2.VideoCapture(0)

# Source points (4 points from the original frame)
pts1 = np.float32([
    [100, 100],      # top-left
    [500, 100],      # top-right
    [100, 400],      # bottom-left
    [500, 400]       # bottom-right
])

# Destination points (where to map them)
pts2 = np.float32([
    [150, 150],
    [450, 120],
    [120, 450],
    [480, 420]
])

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Calculate width & height from frame
    rows, cols = frame.shape[:2]

    # Get perspective transform matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    perspective_frame = cv2.warpPerspective(frame, M, (cols, rows))

    # Display videos
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", perspective_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
