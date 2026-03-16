import cv2
import numpy as np

# Read color image
img = cv2.imread("evening.png")
if img is None:
    print("Image not found!")
    exit()

# Gradient masks
mask1 = np.array([[-1, -2, -1],
                  [ 0,  0,  0],
                  [ 1,  2,  1]])

mask2 = np.array([[-1,  0,  1],
                  [-2,  0,  2],
                  [-1,  0,  1]])

# Apply both masks (color-safe)
grad1 = cv2.filter2D(img, -1, mask1)
grad2 = cv2.filter2D(img, -1, mask2)

# Combine the gradients
gradient = cv2.add(grad1, grad2)

# Sharpen: original + gradient
sharpened = cv2.add(img, gradient)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Gradient Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
