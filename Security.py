import cv2
import winsound
cam = cv2.VideoCapture(0) #select camera
while cam.isOpened(): #works only when camera is open
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #to get rid of the noise
    dilated = cv2.dilate(thresh, None, iterations=3) #to make the slected regioon zoomed
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #To display boxes around object
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)  #It detetects all type of small as well as large movements
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(500,200)
    if cv2.waitKey(10) == ord('q'): #to exit window/camera press q
        break
    cv2.imshow('Security Cam', frame1)