import cv2
import numpy as np

# Read image
img = cv2.imread("evening.png")

# Convert to grayscale for erosion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(gray, kernel, iterations=1)

# Display results
cv2.imshow("Original Image (Color)", img)
cv2.imshow("Eroded Image (Gray)", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
