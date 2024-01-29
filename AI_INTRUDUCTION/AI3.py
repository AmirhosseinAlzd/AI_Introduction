import cv2 

camera = cv2.VideoCapture(0) 

while True: 
    cam , frame = camera.read()
    cv2.imshow("mazda",frame)
    if cv2.waitKey(4000) & 0xff == ord("e"):
        break

