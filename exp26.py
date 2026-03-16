import cv2
import numpy as np

# Read the image in color
img = cv2.imread("image.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 kernel of ones

# Split the image into color channels
b, g, r = cv2.split(img)

# Apply Opening (Erosion followed by Dilation) on each channel
b_opened = cv2.morphologyEx(b, cv2.MORPH_OPEN, kernel)
g_opened = cv2.morphologyEx(g, cv2.MORPH_OPEN, kernel)
r_opened = cv2.morphologyEx(r, cv2.MORPH_OPEN, kernel)

# Merge channels back
opened_img = cv2.merge([b_opened, g_opened, r_opened])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Opened Image", opened_img)

# Save the opened image
cv2.imwrite("opened_output_color.jpg", opened_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
