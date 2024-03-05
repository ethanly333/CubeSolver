import cv2
import numpy as np

blank_path = "./images/cubeInHand2.jpeg"
blank_img = cv2.imread(blank_path)

height, width = blank_img.shape[:2]
#print(height, width)

window_name = "Draw 3x3"

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

image_border = cv2.rectangle(blank_img, start_point1, end_point1, color, thickness)
image_vert1 = cv2.line(image_border, start_point2, end_point2, color, thickness)
image_vert2 = cv2.line(image_border, start_point3, end_point3, color, thickness)
image_horz1 = cv2.line(image_border, start_point4, end_point4, color, thickness)
image_horz2 = cv2.line(image_border, start_point5, end_point5, color, thickness)
image = image_horz2

cv2.imshow(window_name, image)

cv2.waitKey(0)