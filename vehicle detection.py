import cv2
cap = cv2.VideoCapture('C:\\Users\\G TANA CHARY\\Downloads\\Pexels Videos 2103099')
car_cascade = cv2.CascadeClassifier('C:\\Users\\G TANA CHARY\\Desktop\\vehicle detection')
while True:
    ret, frame = cap.read()
    gray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiscale(gray, 1.1, 1)
    for (x, y, w, h) in cars :
        cv2.rectangele(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('video2', frame)
        if cv2.waitkey(33) == 27:
            break
        cv2.destroyAllWindows()
