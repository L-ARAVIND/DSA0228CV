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

# Apply Black Hat (Closing - Original) on each channel
b_blackhat = cv2.morphologyEx(b, cv2.MORPH_BLACKHAT, kernel)
g_blackhat = cv2.morphologyEx(g, cv2.MORPH_BLACKHAT, kernel)
r_blackhat = cv2.morphologyEx(r, cv2.MORPH_BLACKHAT, kernel)

# Merge channels back
blackhat_img = cv2.merge([b_blackhat, g_blackhat, r_blackhat])

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Image", blackhat_img)

# Save the result
cv2.imwrite("blackhat_output_color.jpg", blackhat_img)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
