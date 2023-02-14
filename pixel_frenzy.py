import cv2
import numpy as np

# to play with HSV values. BGR not RGB.
rgb_lol = np.uint8([[[0x00, 0x00, 0xFF]]])
hsv_lol = cv2.cvtColor(rgb_lol, cv2.COLOR_BGR2HSV)
print(hsv_lol) # this output represents full red

# open the image
img = cv2.imread('image.png') # could be jpeg or anything really

# convert the image to the HSV colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define the ROI coordinates. that's the part of the image we are looking at. rest is ignored.
x, y, w, h = 400, 800, 400, 400

# select the ROI
rgb_roi = img[y:y+h, x:x+w] # only to display the exact area / show extracted colors in the end for "debugging"
roi = hsv[y:y+h, x:x+w] # work on this area

# define the lower and upper thresholds for red and green colors
# angle (hue), saturation, value. hue is limited to 0 - 180 degrees.
# angle of red is at 0. +- 10 means checking 170 - 180, and 0 - 10. red is weird.
red_lower = np.array([0, 50, 50])
red_upper = np.array([10, 255, 255])
red_lower2 = np.array([170, 50, 50])
red_upper2 = np.array([180, 255, 255])
green_lower = np.array([50, 50, 50]) # angle of green is around 60. +- 10
green_upper = np.array([70, 255, 255])

# create a mask for red and green colors
mask_red1 = cv2.inRange(roi, red_lower, red_upper)
mask_red2 = cv2.inRange(roi, red_lower2, red_upper2)
# combine both ranges, 0-10 and 170-180 for red
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_green = cv2.inRange(roi, green_lower, green_upper)

# count the number of red and green pixels. just to show how classification could be done.
red_count = np.count_nonzero(mask_red)
green_count = np.count_nonzero(mask_green)

# calculate the percentage of red and green pixels. could be used to classify "red" or "green" or "could not really detect it".
total_pixels = roi.shape[0] * roi.shape[1]
red_percentage = (red_count / total_pixels) * 100
green_percentage = (green_count / total_pixels) * 100

# print the percentages
print(f"Percentage of red pixels: {red_percentage:.2f}%")
print(f"Percentage of green pixels: {green_percentage:.2f}%")

# just for display: show the actual pixels that are red / green, i.e.: take the pixels from the original image, and show those that are red / green
# where the mask is non-zero (i.e. red or green found), the original image is copied
rgb_red = cv2.bitwise_and(rgb_roi, rgb_roi, mask=mask_red)
rgb_green = cv2.bitwise_and(rgb_roi, rgb_roi, mask=mask_green)

# show the images to get a feel. original image, only red parts, only green parts
# see output.png for an example.
cv2.imshow('frame', rgb_roi)
cv2.imshow('mask_red', rgb_red)
cv2.imshow('mask_green', rgb_green)

# wait for keypress. otherwise imshow instantly closes.
k = cv2.waitKey(0) & 0xFF


