import cv2
import numpy as np

# Read image (color)
img = cv2.imread("mikky.png")

if img is None:
    print("Image not found!")
    exit()

# Split the image into B, G, R channels
b, g, r = cv2.split(img)

# Extended Laplacian mask including diagonal neighbors
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]], dtype=np.float32)

# Apply Laplacian on each channel
lap_b = cv2.convertScaleAbs(cv2.filter2D(b, cv2.CV_32F, kernel))
lap_g = cv2.convertScaleAbs(cv2.filter2D(g, cv2.CV_32F, kernel))
lap_r = cv2.convertScaleAbs(cv2.filter2D(r, cv2.CV_32F, kernel))

# Sharpen each channel (original - laplacian)
sharp_b = cv2.subtract(b, lap_b)
sharp_g = cv2.subtract(g, lap_g)
sharp_r = cv2.subtract(r, lap_r)

# Merge sharpened channels to form the final sharpened color image
sharp_color = cv2.merge((sharp_b, sharp_g, sharp_r))

# Display
cv2.imshow("Original (Color)", img)
cv2.imshow("Sharpened Image (Diagonal Mask)", sharp_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
