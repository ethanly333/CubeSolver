import cv2
import numpy as np

#Color thresholds (r,g,b)
min_white = [255, 255, 255]
max_white = [216, 216, 216]
min_yellow = [255, 241, 108]
max_yellow = [182, 164, 0]
min_red = [255, 70, 70]
max_red = [148, 0, 0]
min_orange = [255, 148, 85]
max_orange = [188, 69, 0]
min_blue = [84, 90, 255]
max_blue = [0, 0, 127]
min_green = [98, 255, 98]
max_green = [0, 85, 0]

""" This will load a picture of a scrambled cube and draw a frame around it to extract piece color"""
ref_path = "./images/cubeInHand2.jpeg"
ref_img = cv2.imread(ref_path)

height, width = ref_img.shape[:2]
#print(height, width)

color = (0, 0, 0)
thickness = 12

top_border_x = int((width/2)-750)
top_border_y = int((height/2)-750)
btm_border_x = int((width/2)+750)
btm_border_y = int((height/2)+750)

start_point1 = (top_border_x, top_border_y)
end_point1 = (btm_border_x, btm_border_y)

start_point2 = (top_border_x+500, top_border_y)
end_point2 = (btm_border_x-1000, btm_border_y)

start_point3 = (top_border_x+1000, top_border_y)
end_point3 = (btm_border_x-500, btm_border_y)

start_point4 = (top_border_x, top_border_y+500)
end_point4 = (btm_border_x, btm_border_y-1000)

start_point5 = (top_border_x, top_border_y+1000)
end_point5 = (btm_border_x, btm_border_y-500)

image_border = cv2.rectangle(ref_img, start_point1, end_point1, color, thickness)
image_vert1 = cv2.line(image_border, start_point2, end_point2, color, thickness)
image_vert2 = cv2.line(image_border, start_point3, end_point3, color, thickness)
image_horz1 = cv2.line(image_border, start_point4, end_point4, color, thickness)
image_horz2 = cv2.line(image_border, start_point5, end_point5, color, thickness)
framed_image = image_horz2

cv2.imshow("Reference Image", framed_image)

cv2.waitKey(0)

""" We will now extract piece color 
    Corners: 1-4 (start left -> clockwise)
    Edges: 1-4 (start top -> clockwise)
"""

corner1 = ref_img[top_border_y : top_border_y+500, top_border_x : top_border_x+500]
corner2 = ref_img[top_border_y : top_border_y+500, top_border_x+1000 : top_border_x+1500]
corner3 = ref_img[top_border_y+1000 : top_border_y+1500, top_border_x+1000 : top_border_x+1500]
corner4 = ref_img[top_border_y+1000 : top_border_y+1500, top_border_x : top_border_x+500]

edge1 = ref_img[top_border_y : top_border_y+500, top_border_x+500 : top_border_x+1000]
edge2 = ref_img[top_border_y+500 : top_border_y+1000, top_border_x+1000 : top_border_x+1500]
edge3 = ref_img[top_border_y+1000 : top_border_y+1500, top_border_x+500 : top_border_x+1000]
edge4 = ref_img[top_border_y+500 : top_border_y+1000, top_border_x : top_border_x+500]


"""cv2.imshow("Corner 1", corner1)
cv2.waitKey(0)
cv2.imshow("Corner 2", corner2)
cv2.waitKey(0)
cv2.imshow("Corner 3", corner3)
cv2.waitKey(0)
cv2.imshow("Corner 4", corner4)
cv2.waitKey(0)

cv2.imshow("Edge 1", edge1)
cv2.waitKey(0)
cv2.imshow("Edge 2", edge2) 
cv2.waitKey(0)
cv2.imshow("Edge 3", edge3)
cv2.waitKey(0)
cv2.imshow("Edge 4", edge4)
cv2.waitKey(0)"""

#find the avg color of each piece image
b, g, r = cv2.split(edge4)    # returns as b,g,r
b_avg = cv2.mean(b)[0]
g_avg = cv2.mean(g)[0]
r_avg = cv2.mean(r)[0]
print(int(r_avg),int(g_avg),int(b_avg))

"""
COLOR TABLE:
R:
    Red
G:
    Green
B:
    Blue
WHITE:
    r, g, b are all equal
"""

