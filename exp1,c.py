import cv2

# Read the image
image = cv2.imread(r"mikky.png")

# Check if the image was loaded
if image is None:
    print("Error: Image not found or path is incorrect!")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Canny Edges", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
