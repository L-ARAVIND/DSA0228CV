import cv2
import numpy as np

# Read image
img = cv2.imread("mikky.png")

# Image height & width
rows, cols = img.shape[:2]

# 4 points from the original image (source points)
pts1 = np.float32([
    [50, 50],      # top-left
    [300, 50],     # top-right
    [50, 300],     # bottom-left
    [300, 300]     # bottom-right
])

# 4 points for the final transformed image (destination points)
pts2 = np.float32([
    [10, 100],     # new top-left
    [280, 80],     # new top-right
    [50, 350],     # new bottom-left
    [300, 300]     # new bottom-right
])

# Create perspective transform matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
perspective_img = cv2.warpPerspective(img, M, (cols, rows))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformation", perspective_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
