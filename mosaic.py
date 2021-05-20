import cv2

image_file = "sample.jpg"
cascade_file = "./haarcascades/haarcascade_frontalface_alt.xml"
color = (0,255,0)
image = cv2.imread(image_file,1)

def mosaic(image,scale=0.1):
    h, w = image.shape[:2]
    dst = cv2.resize(image,dsize=None,fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST)
    dst = cv2.resize(dst, dsize=(w, h), interpolation=cv2.INTER_NEAREST)
    
    return dst

cv2.imshow('original',image)
cv2.waitKey(0)

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray",image_gray)
cv2.waitKey(0)

cascade = cv2.CascadeClassifier(cascade_file)

front_face_list = cascade.detectMultiScale(image_gray,minSize = (30,30))

if len(front_face_list) > 0:
    for (x,y,w,h) in front_face_list:
        roi = image[y : y + h, x : x + w]
        roi[:] = mosaic(roi)
    cv2.imshow('mosaic', image)
    cv2.waitKey(0)
    
if len(front_face_list) > 0:
    for (x,y,w,h) in front_face_list:
        print("[x,y] = "+ str(x) + "," + str(y) + "[w,h] =" + str(w) + "," + str(h))
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=10)
    cv2.imshow('range', image)
    cv2.waitKey(0)
else:
    print("No human")
