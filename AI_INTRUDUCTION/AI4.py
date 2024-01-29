import cv2 

camera = cv2.VideoCapture(0)  

face_cascade = cv2.CascadeClassifier('AI files-teachers/face.xml')
eye_cascade = cv2.CascadeClassifier('AI files-teachers/eye.xml')

while True:

    cam , frame = camera.read()

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(gray_frame,1.3,5)

    for (x,y,w,h) in face:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=4)

        gray_face=gray_frame[y:y+h,x:x+w]

        color_face=frame[y:y+h,x:x+w]

        eye=eye_cascade.detectMultiScale(gray_face,1.3,5) 
        for (a,b,c,d) in eye:

            cv2.rectangle(color_face,(a,b),(a+c,b+d),(0,255,0),thickness=4)

    cv2.imshow("windowname",frame)

    if cv2.waitKey(1) & 0xff == ord("e"):  
        break

