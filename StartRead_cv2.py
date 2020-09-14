import cv2

cap=cv2.VideoCapture(0)

cv2.startWindowThread()

while True:
    _,frame=cap.read()
    cv2.imshow("Original",frame)
    
    gray_original=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Originalgray",gray_original)
    
    original=cv2.flip(frame,1)
    cv2.imshow("Inversion",original)
    
    gray=cv2.cvtColor(original,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Binarization",gray)
    
    #gray_original=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Originalgray",gray_original)
    
    k=cv2.waitKey(0) & 0xFF
    if k==27:
        break
        
        
cv2.waitKey(1)
cv2.destroyALLWindows()
cv2.waitKey(1)
