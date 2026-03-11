import cv2
import numpy as np

# Read image (color)
img = cv2.imread("house.png")

if img is None:
    print("Image not found!")
    exit()

# Positive center Laplacian kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# Apply filter directly on color image
sharp = cv2.filter2D(img, -1, kernel)

# Display
cv2.imshow("Original (Color)", img)
cv2.imshow("Sharpened (Positive Center Mask)", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
