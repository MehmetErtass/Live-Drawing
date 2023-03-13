# Adding the libraries to be used
import cv2
import numpy as np

def sketch(image):

    # height of the image
    height=int(image.shape[0])
    
    # width of image
    width=int(image.shape[1])
    
    # storing the image dimension
    dim=(width,height)
    
    # resize the image into our own dimension
    resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    
    # applying a kernel
    kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    
    #sharpning the resized image
    sharp=cv2.filter2D(resize,-1,kernel)
    
    #converting the image into gray scale
    gray=cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)
    inv=255-gray
    
    #apply bluring
    blur=cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)
    
    #draw sketch    
    s=cv2.divide(gray,255-blur,scale=256)
    return s

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    cv2.imshow('Live_Sketch',sketch(frame))
    cv2.imshow('Live_image',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
