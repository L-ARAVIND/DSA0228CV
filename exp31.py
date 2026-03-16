import cv2
import numpy as np

# Load the main image and the template image
scene = cv2.imread(r"watch.png")  # the larger image
template = cv2.imread(r"watch.png")  # the watch template

if scene is None or template is None:
    print("Error: One or both images not found!")
    exit()

# Convert images to grayscale
scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get width and height of the template
w, h = template_gray.shape[::-1]

# Apply template matching
res = cv2.matchTemplate(scene_gray, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8  # adjust 0.8 to higher/lower for detection sensitivity
loc = np.where(res >= threshold)

# Draw rectangles around matched areas
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(scene, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Show result
cv2.imshow("Detected Watch", scene)
cv2.imwrite(r"C:\openCV exp\watch_detected.png", scene)

cv2.waitKey(0)
cv2.destroyAllWindows()
