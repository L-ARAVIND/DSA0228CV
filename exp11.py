import cv2
import numpy as np

# ---- Step 1: Read Image ----
img = cv2.imread("flower.png")
rows, cols = img.shape[:2]

# ---- Step 2: Source and Destination Points ----
# 4 points from original image
pts_src = np.array([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
], dtype=float)

# 4 points where we want them to move
pts_dst = np.array([
    [80, 120],
    [260, 80],
    [100, 350],
    [320, 300]
], dtype=float)

# ---- Step 3: Build matrix A using DLT ----
A = []
for i in range(4):
    x, y = pts_src[i][0], pts_src[i][1]
    u, v = pts_dst[i][0], pts_dst[i][1]

    A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
    A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])

A = np.array(A)

# ---- Step 4: Solve using SVD ----
U, S, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)    # Last row gives solution

# Normalize matrix
H = H / H[2, 2]

# ---- Step 5: Apply Transformation ----
output = cv2.warpPerspective(img, H, (cols, rows))

# ---- Step 6: Display ----
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
