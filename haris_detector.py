import numpy as np
import cv2
import glob
import math


def euclid(a, b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def harris_detector(image_url = 'abc.jpg') :
    img  = cv2.imread(image_url)
    img = cv2.resize(img, (0,0),fx = 0.1 , fy = 0.1)
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    temp = img
    dst = cv2.cornerHarris(gray,6,7,0.04)
    dst =cv2.dilate(dst,None)
    dst1 = np.array([dst > 0.07*dst.max()]).reshape(dst.shape)
    dst1 = np.argwhere(dst1)
    ppt = [list(dst1[0])]
    thres = 50
    latest = dst1[0]
    for i in range(1,dst1.shape[0]):
        if(euclid(latest,dst1[i])) > thres:
            ppt.append(dst1[i])
            latest = dst1[i]
    ppt1 = [ppt[0]]
    for i in range(1,len(ppt)):
        b = True
        for element in ppt1 :
            if euclid(element , ppt[i]) <= thres :
                b = False
        if b == True : ppt1.append(ppt[i])
            
    print(list(ppt1))
    
    temp2 = img
    for pix in ppt1 :
        temp2[pix[0],pix[1]] = [0,0,255]
    return temp2


    