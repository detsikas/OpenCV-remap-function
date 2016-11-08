#!/Users/me/anaconda2/envs/opencv/bin/python
import cv2
import sys
import numpy as np
import time

def rippleEffect (inputImage, outputImage, mapX, mapY):
    cv2.remap(inputImage, mapX, mapY, cv2.INTER_LINEAR, outputImage, cv2.BORDER_REPLICATE)

if len(sys.argv)!=2:
    print "Usage "+sys.argv[0]+" <filename>"
    sys.exit()

# Read input image
inputImage = cv2.imread(sys.argv[1])
cv2.imshow("Input image", inputImage)
cv2.waitKey(0)

# Create output image
outputImage = np.zeros((inputImage.shape[0], inputImage.shape[1],
                        inputImage.shape[2]), inputImage.dtype)

# Ripple paramters
A = 10.0                        # Ripple magnitute
f = np.pi*2/inputImage.shape[0]     # Ripple frequency
p = 3.0*np.pi/4.0               # Ripple phase
direction = (1.0/5.0)*np.pi/2.0 # Ripple direction

mapX = np.zeros((inputImage.shape[0], inputImage.shape[1]), dtype=np.float32)
mapY = np.zeros((inputImage.shape[0], inputImage.shape[1]), dtype=np.float32)

while(1):
    for m in range(100):
        p = m*5.0*np.pi/100 + np.pi
        begin = time.clock()
        for j in range(inputImage.shape[0]):
            for i in range(inputImage.shape[1]):
                mapX[j,i] = i+A*(i/inputImage.shape[1])*np.sin(f*j+p)*np.cos(direction)
                mapY[j,i] = j+A*np.sin(f*i+p)*np.sin(direction)        
        end = time.clock()
        print "Duration of map filling: "+str((end-begin)*1000)+"ms"
        begin2 = time.clock()
        rippleEffect(inputImage, outputImage, mapX, mapY)
        end2 = time.clock()
        print "Duration of ripple application: "+str((end2-begin2)*1000)+"ms"
        cv2.imshow("Output image", outputImage)
        cv2.waitKey(1)
