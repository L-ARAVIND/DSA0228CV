import cv2

# Read image
img = cv2.imread("mikky.png")

# Get image height and width
h, w = img.shape[:2]

# Rotation – Clockwise 90 degrees
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotation – Counter Clockwise 90 degrees
counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
