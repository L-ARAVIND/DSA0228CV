import cv2
import numpy as np

# Read the image in color
img = cv2.imread("evening.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 kernel of ones

# Split the image into color channels
b, g, r = cv2.split(img)

# Apply Dilation to each channel
b_dilated = cv2.dilate(b, kernel, iterations=1)
g_dilated = cv2.dilate(g, kernel, iterations=1)
r_dilated = cv2.dilate(r, kernel, iterations=1)

# Merge channels back
dilated_img = cv2.merge([b_dilated, g_dilated, r_dilated])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_img)

# Save the dilated image
cv2.imwrite("dilated_output_color.jpg", dilated_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
