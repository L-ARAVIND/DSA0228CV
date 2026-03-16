import cv2

# Load the image
img = cv2.imread("flower.png")
if img is None:
    print("Image not found!")
    exit()

# Define crop region (e.g., top-left corner)
x, y, w, h = 50, 50, 150, 150  # Adjust these values as needed
cropped_region = img[y:y+h, x:x+w]

# Define paste location (e.g., bottom-right corner)
paste_x, paste_y = img.shape[1] - w - 50, img.shape[0] - h - 50

# Paste the cropped region into the new location
img[paste_y:paste_y+h, paste_x:paste_x+w] = cropped_region

# Display the result
cv2.imshow("Cropped and Pasted Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()