import cv2
import numpy as np

# Read image
img = cv2.imread("evening.png")

# How much to move the image
tx = 100   # move right by 100 pixels
ty = 50    # move down by 50 pixels

# Translation matrix
T = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
moved_img = cv2.warpAffine(img, T, (img.shape[1], img.shape[0]))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
