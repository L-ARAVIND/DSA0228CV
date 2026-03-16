import cv2
import numpy as np

# Read the image in color
img = cv2.imread("mikky.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 kernel

# Split the image into color channels
b, g, r = cv2.split(img)

# Apply Top Hat (original - Opening) on each channel
b_tophat = cv2.morphologyEx(b, cv2.MORPH_TOPHAT, kernel)
g_tophat = cv2.morphologyEx(g, cv2.MORPH_TOPHAT, kernel)
r_tophat = cv2.morphologyEx(r, cv2.MORPH_TOPHAT, kernel)

# Merge channels back
tophat_img = cv2.merge([b_tophat, g_tophat, r_tophat])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat Image", tophat_img)

# Save the result
cv2.imwrite("tophat_output_color.jpg", tophat_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
