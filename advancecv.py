import cv2
import numpy as np

drawing = False

ix, iy = -1, -1

img = np.zeros((512, 512, 3), dtype=np.uint8)

def draw(event, x, y, flags, param):

    global ix, iy, drawing, img

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x, y

    # Mouse moving
    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing == True:

            temp_img = img.copy()

            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 2)

            cv2.imshow("AdvanceCV", temp_img)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False

        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

cv2.namedWindow("AdvanceCV")

cv2.setMouseCallback("AdvanceCV", draw)

while True:

    cv2.imshow("AdvanceCV", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()