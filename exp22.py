import cv2

# Read the main image
img = cv2.imread("mikky.png")
if img is None:
    print("Image not found!")
    exit()

# Watermark text
text = "micky mouse"

# Choose position (bottom-right)
h, w = img.shape[:2]
position = (w - 300, h - 20)

# Add text watermark (Black color)
watermarked = img.copy()
cv2.putText(watermarked, text, position,
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2, (0, 0, 0), 3, cv2.LINE_AA)

# Display
cv2.imshow("Original", img)
cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
