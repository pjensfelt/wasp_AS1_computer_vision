import numpy as np
import cv2 as cv

# The path to (relative to where jupyter is running) the image to load
imageName = "test_images/image1.jpg"

# Load the source image
image = cv.imread(imageName)

# We can comvert the image directly to gray scale if we want.
# We do that??? Well, in many cases the algorithm we want to run is not using the color information.
# cv2.IMREAD_COLOR (1)     : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE (0) : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED (-1): Loads image as such including alpha channel
imageG = cv.imread(imageName, cv.IMREAD_GRAYSCALE)

print("We remind ourself about the fact that images are merely matrices with numbers")
print(imageG)

# Show the gray scale image
cv.imshow('Gray scale image',imageG)

# Show the color image
cv.imshow('Color image', image)

print("The first image window proably ended up below the second one")
print("Waiting for the user to press ENTER with one of the image windows active")
cv.waitKey(0)
cv.destroyAllWindows()
