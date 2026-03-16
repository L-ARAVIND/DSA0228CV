import cv2

# Load the pre-trained Haar cascade for face detection
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Load the image
image_path = r"rohit.webp"  # Replace with your image path
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale (required by Haar cascade)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the output
cv2.imshow("Face Detection", img)
cv2.imwrite(r"C:\openCV exp\face_detected.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
