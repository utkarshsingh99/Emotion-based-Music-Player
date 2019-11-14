import cv2
x = cv2.VideoCapture(0)
output , photo = x.read()
cv2.imwrite("emotions.png" , photo)
x.release()
