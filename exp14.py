import cv2
import numpy as np

# Read the image
img = cv2.imread("mikky.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit for display
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y-axis Edges", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
