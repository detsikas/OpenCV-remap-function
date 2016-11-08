#!/Users/me/anaconda2/envs/opencv/bin/python
import cv2
import sys
import numpy as np
import time

def rippleEffect (inputImage, outputImage, mapX, mapY):
    cv2.remap(inputImage, mapX.astype(np.float32), mapY.astype(np.float32), cv2.INTER_LINEAR, outputImage, cv2.BORDER_REPLICATE)

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

# Ripple parameters
A = 10.0                        # Ripple magnitute
omega = np.pi*2/inputImage.shape[0]     # Ripple frequency
p = 3.0*np.pi/4.0               # Ripple phase
direction = (1.0/5.0)*np.pi/2.0 # Ripple direction
rippleFrames = 100

# Integer ranges used to construct the mapping matrices
jrange = np.arange(inputImage.shape[0])
irange = np.arange(inputImage.shape[1])
while(1):
    for m in range(rippleFrames):
        p = m*2.0*np.pi/rippleFrames + np.pi
        begin = time.clock()

        #mapX matrix construction
        mapX1 = np.tile(A*np.cos(direction)*irange/inputImage.shape[1] , (inputImage.shape[0],1))
        mapX2 = np.tile((np.sin(omega*jrange+p)), (inputImage.shape[1],1)).transpose()
        mapX = np.multiply(mapX1, mapX2) + np.tile(irange, (inputImage.shape[0],1))
        #mapY matrix construction
        mapY1 = np.tile(A*np.sin(omega*irange+p)*np.sin(direction), (inputImage.shape[0],1))
        mapY2 = np.tile(jrange, (inputImage.shape[1],1)).transpose()
        mapY = mapY1 + mapY2

        ''' mapX and mapY construction with loops instead of numpy
        for j in range(inputImage.shape[0]):
            for i in range(inputImage.shape[1]):
                mapX[j,i] = i+A*(i/inputImage.shape[1])*np.sin(f*j+p)*np.cos(direction)
                mapY[j,i] = j+A*np.sin(f*i+p)*np.sin(direction)
        '''
        
        end = time.clock()
        print "Duration of map filling: "+str((end-begin)*1000)+"ms"
        begin2 = time.clock()
        rippleEffect(inputImage, outputImage, mapX, mapY)
        end2 = time.clock()
        print "Duration of ripple application: "+str((end2-begin2)*1000)+"ms"
        cv2.imshow("Output image", outputImage)
        cv2.waitKey(1)
