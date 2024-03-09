import cv2 
import numpy as np

# REFERENCE
ref_img = cv2.imread('./images/ref_cube7.jpeg')
cv2.imshow("Reference", ref_img)
cv2.waitKey(0)

# GRAYSCALE 
grey_ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", grey_ref_img)
cv2.waitKey(0)

# GAUSSIAN BLUR›
blur_ref_img = cv2.GaussianBlur(grey_ref_img, (3,3), 0)
cv2.imshow("Gaussian Blur", blur_ref_img)
cv2.waitKey(0)

# SOBEL EDGE DETECTION (Not used)
sobelx = cv2.Sobel(src=blur_ref_img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=blur_ref_img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=blur_ref_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

# Canny Edge Detection
canny_img = cv2.Canny(image=ref_img, threshold1=100, threshold2=200)
cv2.imshow("Canny", canny_img)
cv2.waitKey(0)

# Image Dilation
kernel = np.ones((5,5), np.uint8)
dilation_img = cv2.dilate(canny_img, kernel, iterations=3)
cv2.imshow("Dilation", dilation_img)
cv2.waitKey(0)

# Find Contours
ref_copy = ref_img.copy()
_, thresh = cv2.threshold(dilation_img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

skip = 0
for contour in contours:

    # ignore the first iteration as the first contour is the whole image
    if skip == 0:
        skip = 1
        continue

    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) 
    cv2.drawContours(ref_copy, [contour], 0, (0, 0, 255), 5) 

    M = cv2.moments(contour) 
    if M['m00'] != 0.0: 
        x = int(M['m10']/M['m00']) 
        y = int(M['m01']/M['m00']) 

    if len(approx) == 4: 
        cv2.putText(ref_copy, 'Square', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3) 
  

cv2.imshow("Contours", ref_copy)
cv2.waitKey(0)