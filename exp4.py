import cv2

# Read image
img = cv2.imread("image.png")

# Smaller size (50% of original)
small_img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Bigger size (200% of original)
big_img = cv2.resize(img, None, fx=2, fy=2)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image", small_img)
cv2.imshow("Bigger Image", big_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
