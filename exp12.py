import cv2

# Read the image
img = cv2.imread("image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
