import cv2

# Load the image
image_path = r"virat.webp"  # Replace with your image path
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Define the rectangle coordinates (x, y, width, height)
x, y, w, h = 100, 50, 200, 200  # Change according to the object location

# Draw rectangle on the original image
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Extract the object inside the rectangle
extracted_object = img[y:y+h, x:x+w]

# Show images
cv2.imshow("Original Image with Rectangle", img)
cv2.imshow("Extracted Object", extracted_object)

# Save the extracted object
cv2.imwrite(r"C:\openCV exp\extracted_object.jpg", extracted_object)

cv2.waitKey(0)
cv2.destroyAllWindows()
