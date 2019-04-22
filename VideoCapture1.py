import cv2, time, pandas
from datetime import datetime

video = cv2.VideoCapture(0)

#1. Capture First Image
# check, frame=video.read()

# print(check)
# print(frame)
# time.sleep(3)
# cv2.waitKey(0)
# video.release()
# cv2.destroyAllWindows()

#2. Capture Image Continuously
while True:
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing...",gray)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()