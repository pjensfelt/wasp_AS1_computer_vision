import numpy as np
import cv2 as cv
import sys
import signal


# When working wth a live stream we need a way to stop 
# when we are done. To do so gracefully we want to trap 
# pressing ctrl-c and clen things up, for example, 
# by reasing the capture device.
def signal_handler(signal, frame):
    # KeyboardInterrupt detected, exiting
    global is_interrupted
    is_interrupted = True


# You want to change the device number if you have 
# more than one camera. The built-in, if you have such, 
# will typically be number 0, the next one would be 1, 
# and so on.
#
# NOTE Do not forget to relase the capture device when you are done

device_number = 0
capture_device = cv.VideoCapture(device_number)

if capture_device.isOpened(): # try to get the first frame
    is_capturing, image = capture_device.read()
else:
    is_capturing = False
    print("Failed to get even a single image frame")
    sys.exit()

# Register a signal handler which will deal with pressing ctrl-c
signal.signal(signal.SIGINT, signal_handler)
is_interrupted = False

# Loop for as long as we get images (and no one pressed ctrl-c this is tested in the loop)
while is_capturing:

	# Capture the image
    is_capturing, image = capture_device.read()

    # Show the image
    cv.imshow("Image stream", image)

    # Wait for a while until we grab the next image
    time_to_wait_ms = 50
    cv.waitKey(time_to_wait_ms)

    if is_interrupted:
    	print("Ctrl-c pressed")
    	break

print("Ending by releasing the device")
cv.destroyAllWindows()
capture_device.release()
