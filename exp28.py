import cv2
import numpy as np

# Read the image in color
img = cv2.imread("flower.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 kernel

# Split the image into color channels
b, g, r = cv2.split(img)

# Apply Morphological Gradient (Dilation - Erosion) on each channel
b_gradient = cv2.morphologyEx(b, cv2.MORPH_GRADIENT, kernel)
g_gradient = cv2.morphologyEx(g, cv2.MORPH_GRADIENT, kernel)
r_gradient = cv2.morphologyEx(r, cv2.MORPH_GRADIENT, kernel)

# Merge channels back
gradient_img = cv2.merge([b_gradient, g_gradient, r_gradient])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient Image", gradient_img)

# Save the result
cv2.imwrite("gradient_output_color.jpg", gradient_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
