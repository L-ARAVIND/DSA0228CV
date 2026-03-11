import cv2
import numpy as np

# Read image
img = cv2.imread("mikky.png")

# Image height & width
rows, cols = img.shape[:2]

# 4 points in the original image
pts1 = np.float32([
    [50, 50],      # top-left
    [300, 50],     # top-right
    [50, 300],     # bottom-left
    [300, 300]     # bottom-right
])

# 4 points in the output image (destination)
pts2 = np.float32([
    [10, 100],
    [280, 80],
    [50, 350],
    [300, 300]
])

# Compute homography matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply the homography transformation
homography_img = cv2.warpPerspective(img, H, (cols, rows))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", homography_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
