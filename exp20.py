import cv2
import numpy as np

# Read image
img = cv2.imread("image.png")

if img is None:
    print("Image not found!")
    exit()

# Set high-boost value
A = 2  # You can increase A for stronger sharpening

# High-boost mask using 4-neighbors (A + 4 in center)
kernel = np.array([[0, -1, 0],
                   [-1, A + 4, -1],
                   [0, -1, 0]], dtype=np.float32)

# Apply high-boost filtering on color image
highboost = cv2.filter2D(img, -1, kernel)

# Display
cv2.imshow("Original (Color)", img)
cv2.imshow(f"High-Boost Sharpened (A={A})", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
