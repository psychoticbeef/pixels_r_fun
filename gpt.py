# Three queries for chatGPT:

# Write Python code with OpenCV loads a local image, and checks a ROI for green or red color. Take into account that the hue of red is 170-180 as well as 0-10. Calculate the percentage of red pixels and the percentage of green pixels. Make the ROI easily configurable at the start. Same for saturation and value for green and red.

# Please add a configuration option: If percentage is below a certain threshold (that's the parameter), then print "unsure", else print which color has the higher percentage.

# Can you reduce the percentage_threshold check to only check once? It should be possible to check for that first, then check the rest with elif.

import cv2

# Define the HSV ranges for red and green colors
red_lower = (0, 70, 50)
red_upper = (10, 255, 255)
red_lower2 = (170, 70, 50)
red_upper2 = (180, 255, 255)
green_lower = (40, 70, 50)
green_upper = (80, 255, 255)

# Define the ROI (region of interest) coordinates
roi_x = 400
roi_y = 800
roi_w = 400
roi_h = 400

# Define the percentage threshold for the color detection
percentage_threshold = 5

# Load the image
img = cv2.imread('image.png')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a mask for the red color in the ROI
mask_red = cv2.inRange(hsv[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w], red_lower, red_upper)
mask_red2 = cv2.inRange(hsv[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w], red_lower2, red_upper2)
mask_red = cv2.bitwise_or(mask_red, mask_red2)

# Create a mask for the green color in the ROI
mask_green = cv2.inRange(hsv[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w], green_lower, green_upper)

# Calculate the percentage of red and green pixels in the ROI
total_pixels = roi_w * roi_h
red_pixels = cv2.countNonZero(mask_red)
green_pixels = cv2.countNonZero(mask_green)
red_percentage = round(red_pixels / total_pixels * 100, 2)
green_percentage = round(green_pixels / total_pixels * 100, 2)

# Determine which color has the higher percentage
if red_percentage < percentage_threshold and green_percentage < percentage_threshold:
    print("unsure")
elif red_percentage > green_percentage:
    print("red")
elif green_percentage > red_percentage:
    print("green")
else:
    print("equal")

