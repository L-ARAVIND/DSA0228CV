import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread("image.png", 0)   # 0 → read in grayscale

# Step 2: Apply Sobel along X-axis
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Step 3: Apply Sobel along Y-axis
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Step 4: Combine X + Y edges
sobel_xy = cv2.magnitude(sobel_x, sobel_y)

# Step 5: Convert back to uint8 (0–255)
sobel_xy = np.uint8(sobel_xy)

# Step 6: Show output
cv2.imshow("Sobel XY Edge Detection", sobel_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
