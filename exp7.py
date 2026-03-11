import cv2
import numpy as np

# Read image
img = cv2.imread("image.png")

# Image height and width
rows, cols = img.shape[:2]

# 3 points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# 3 points in the new transformed image
pts2 = np.float32([[70, 100], [220, 80], [80, 250]])

# Get affine transform matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transform
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Display output
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", affine_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
