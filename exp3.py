import cv2

# Open webcam (0 = default camera)
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Show NORMAL speed video
    cv2.imshow("Normal Video", frame)

    # Show SLOW motion (Higher delay = slower)
    cv2.imshow("Slow Motion Video", frame)

    # Show FAST motion (Lower delay = faster)
    cv2.imshow("Fast Motion Video", frame)

    # Normal speed (wait 1 ms)
    cv2.waitKey(1)

    # Slow motion window → delay 80 ms
    if cv2.waitKey(80) & 0xFF == ord('s'):
        break

    # Fast motion window → delay 1 ms (very fast)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

    # Press 'q' to quit all windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
