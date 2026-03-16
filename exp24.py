import cv2
import numpy as np

# Read the image in color
img = cv2.imread("mikky.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Define Laplacian kernel for boundary detection
kernel = np.array([[ -1, -1, -1],
                   [ -1,  8, -1],
                   [ -1, -1, -1]])

# Split the image into its color channels
b, g, r = cv2.split(img)

# Apply convolution to each channel
b_edge = cv2.filter2D(b, -1, kernel)
g_edge = cv2.filter2D(g, -1, kernel)
r_edge = cv2.filter2D(r, -1, kernel)

# Merge channels back
boundary_img = cv2.merge([b_edge, g_edge, r_edge])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary_img)

# Save the boundary image
cv2.imwrite("boundary_output_color.jpg", boundary_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
