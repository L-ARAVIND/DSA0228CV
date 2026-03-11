import cv2
import numpy as np

# Read image
img = cv2.imread("image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator along X-axis
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Convert back to unsigned 8-bit
sobel_x = cv2.convertScaleAbs(sobel_x)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X-axis Edges", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
