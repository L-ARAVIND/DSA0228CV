import cv2
import numpy as np

# Read image
img = cv2.imread("mikky.png")

if img is None:
    print("Image not found!")
    exit()

# Step 1: Blur the image (Gaussian Blur)
blur = cv2.GaussianBlur(img, (9, 9), 0)

# Step 2: Create mask = original - blurred
mask = cv2.subtract(img, blur)

# Step 3: Add scaled mask to original to get sharpened result
k = 1.5   # sharpening amount
sharp = cv2.addWeighted(img, 1 + k, blur, -k, 0)

# Display all results
cv2.imshow("Original (Color)", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Unsharp Mask", mask)
cv2.imshow("Sharpened (Unsharp Masking)", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
