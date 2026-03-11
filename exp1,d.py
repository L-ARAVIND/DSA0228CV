import cv2
import numpy as np

# Read image
img = cv2.imread(r"flower.png")

# Convert to grayscale for dilation
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(gray, kernel, iterations=1)

# Display results
cv2.imshow("Original Image (Color)", img)
cv2.imshow("Dilated Image (Gray)", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
