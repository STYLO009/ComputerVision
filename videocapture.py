import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# HOG Descriptor
hog = cv2.HOGDescriptor()

# Default human detector
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize for better speed
    frame = cv2.resize(frame, (1000, 700))

    # Detect humans
    humans, weights = hog.detectMultiScale(
        frame,
        winStride=(8,8),
        padding=(15,15),
        scale=1.5
    )

    # Draw rectangles
    for (x, y, w, h) in humans:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            "Human",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Human Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()