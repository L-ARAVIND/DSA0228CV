import cv2

# Read the image
image = cv2.imread(r"house.png")

# Check if the image was loaded
if image is None:
    print("Error: Image not found or path is incorrect!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display original and blurred image
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
