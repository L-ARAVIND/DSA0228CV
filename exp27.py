import cv2
import numpy as np

# Read the image in color
img = cv2.imread("mikky.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 kernel of ones

# Split the image into color channels
b, g, r = cv2.split(img)

# Apply Closing (Dilation followed by Erosion) on each channel
b_closed = cv2.morphologyEx(b, cv2.MORPH_CLOSE, kernel)
g_closed = cv2.morphologyEx(g, cv2.MORPH_CLOSE, kernel)
r_closed = cv2.morphologyEx(r, cv2.MORPH_CLOSE, kernel)

# Merge channels back
closed_img = cv2.merge([b_closed, g_closed, r_closed])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Closed Image", closed_img)

# Save the closed image
cv2.imwrite("closed_output_color.jpg", closed_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
