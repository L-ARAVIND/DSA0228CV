import cv2

# ----------- Read the captured video -----------
video = cv2.VideoCapture("clip.mp4")   # Change file name if needed

if not video.isOpened():
    print("Error: Cannot open video file")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break

    # ---------- Normal Video ----------
    cv2.imshow("Normal Video", frame)

    # ---------- Slow Motion ----------
    # Larger delay → slower playback (80 ms)
    cv2.imshow("Slow Motion Video", frame)
    cv2.waitKey(80)

    # ---------- Fast Motion ----------
    # Smaller delay → faster playback (1 ms)
    cv2.imshow("Fast Motion Video", frame)
    cv2.waitKey(1)

    # Press 'q' to exit all
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
