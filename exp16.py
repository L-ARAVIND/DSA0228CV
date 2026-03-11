import cv2
import numpy as np

# Read color image
img = cv2.imread("image.png")

if img is None:
    print("Image not found!")
    exit()

# Split BGR channels
b, g, r = cv2.split(img)

# Laplacian kernel (negative center)
kernel = np.array([[0, 1, 0],
                   [1,-4, 1],
                   [0, 1, 0]], dtype=np.float32)

# Apply Laplacian on each channel
lap_b = cv2.convertScaleAbs(cv2.filter2D(b, cv2.CV_32F, kernel))
lap_g = cv2.convertScaleAbs(cv2.filter2D(g, cv2.CV_32F, kernel))
lap_r = cv2.convertScaleAbs(cv2.filter2D(r, cv2.CV_32F, kernel))

# Sharpen each channel (add Laplacian)
sharp_b = cv2.add(b, lap_b)
sharp_g = cv2.add(g, lap_g)
sharp_r = cv2.add(r, lap_r)

# Merge channels back to color
sharp_color = cv2.merge((sharp_b, sharp_g, sharp_r))

# Display images
cv2.imshow("Original (Color)", img)
cv2.imshow("Sharpened Image (Color)", sharp_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
