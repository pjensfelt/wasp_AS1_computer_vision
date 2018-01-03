import numpy as np
import cv2 as cv
import sys

# Now we capture the image. 
# You want to change the device number if you have 
# more than one camera. The built-in, if you have such, 
# will typically be number 0, the next one would be 1, 
# and so on.
#
# NOTE Do not forget to relase the capture device when you are done

device_number = 0
capture_device = cv.VideoCapture(device_number)

if capture_device.isOpened(): # try to get an image frame
    is_capturing, image = capture_device.read()
else:
    is_capturing = False
    print("Could not capture a frame")
    sys.exit(0)

# Make sure to remember to release the capture device, otherwise you will not be able to get any more images
capture_device.release()


# Show the image
cv.imshow('Color image', image)

print("Wating for the user to press ENTER with one of the image windows active")
cv.waitKey(0)
cv.destroyAllWindows()