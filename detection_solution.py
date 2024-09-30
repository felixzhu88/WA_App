import cv2
import numpy as np

# load image
image = cv2.imread('red.png')

# convert the colors to HSV color space 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define HSV range for red
lower_red1 = np.array([0, 160, 160])  
upper_red1 = np.array([10, 240, 240]) 

# create masking for red
mask = cv2.inRange(hsv, lower_red1, upper_red1)

result = cv2.bitwise_and(image, image, mask=mask)

# create contours from the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# debugging, showing where the contours are
# Draw all contours on the image
cv2.drawContours(image, contours, -1, (255, 0, 0), 2)  
cv2.imwrite('contours_found.png', image)

# Set a minimum contour area to filter small objects
min_contour_area = 50 # to get as many cones as I can
center_points = []

# find center of contours (black dots)
for i in contours:
    area = cv2.contourArea(i)
    if area > min_contour_area:
        M = cv2.moments(i)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])  
            cY = int(M["m01"] / M["m00"])  
            center_points.append((cX, cY))
            cv2.circle(image, (cX, cY), 5, (0, 0, 0), -1)

# draw lines!
# stores the center of the cones
left_centers = []
right_centers = []

# find width of image to know where to split the image in half 
# (to seperate left and right cones)
image_width = image.shape[1]

# sorts the points into either left or right
for cX, cY in center_points:
    if cX < image_width / 2:  # Left side
        left_centers.append((cX, cY))
    else:  # Right side
        right_centers.append((cX, cY))

# Draw fitted line for left centers
if len(left_centers) > 1:  # check: need at least two points for line
    # fits line with centers and extend to edges of image
    points = np.array(left_centers, dtype=np.float32)
    [vx, vy, x, y] = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)
    left_y = 0  
    right_y = image.shape[0] 
    left_x = int(x - (y - left_y) * (vx / vy))  
    right_x = int(x + (right_y - y) * (vx / vy)) 
    # draw line
    cv2.line(image, (left_x, left_y), (right_x, right_y), (0, 255, 0), 2)  

# Draw fitted line for right centers
if len(right_centers) > 1:  # check: need at least two points for line
    # fits line with centers and extend to edges of image
    points = np.array(right_centers, dtype=np.float32)
    [vx, vy, x, y] = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)
    left_y = 0  
    right_y = image.shape[0]  
    left_x = int(x - (y - left_y) * (vx / vy))  
    right_x = int(x + (right_y - y) * (vx / vy))  
    # draw line
    cv2.line(image, (left_x, left_y), (right_x, right_y), (0, 255, 0), 2)

# answer image
cv2.imwrite('answer.png', image)
