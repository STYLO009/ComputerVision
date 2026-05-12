import cv2
import numpy as np

def draw(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)

img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.namedWindow("test")
cv2.setMouseCallback("test", draw)

while True:

    cv2.imshow("test", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()