import cv2

# --- Replace this path with your video file path ---
video_path = r"clip.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

# Get total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Read and display frames in reverse
for i in range(total_frames-1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)  # Move to frame i
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow("Reverse Video", frame)

    # Adjust waitKey for speed (25 ms ~ 25 FPS)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
