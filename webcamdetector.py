import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    timer = cv2.getTickCount()
    _, img = cap.read()
    # DETECTING WORDS
    boxes = pytesseract.image_to_data(img)
    for a, b in enumerate(boxes.splitlines()):
        print(b)
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), 3)
                cv2.putText(img, b[11], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 3)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    print(fps)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

