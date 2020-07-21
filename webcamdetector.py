import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('cursive.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def captureScreen(bbox=(300, 300, 1500, 1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr


while True:
    timer = cv2.getTickCount()
    _, img = cap.read()
    # img = captureScreen()
    # DETECTING CHARACTERES
    boxes = pytesseract.image_to_data(img)
    for a, b in enumerate(boxes.splitlines()):
        print(b)
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)
                cv2.putText(img, b[11], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    print(fps)
# cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break