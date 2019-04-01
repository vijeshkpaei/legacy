import string, os
#import os
import pdb
def find_x(bbox_left,image_width,box_xmax):
    image_width = 1.0 * int(image_width)
    absolute_x = int(bbox_left) + 0.5 * (int(box_xmax) - int(bbox_left))
    x = absolute_x / image_width
    x = x * 1.0
    return str(x)

def find_y(image_height,box_ymax,bbox_top):
    image_height = 1.0 * int(image_height)
    absolute_y = int(bbox_top) + 0.5 * (int(box_ymax) - int(bbox_top))
    y = absolute_y / image_height
    y = y * 1.0
    return str(y)
def find_width(box_xmax,bbox_left,image_width): 
    absolute_width = int(box_xmax) - int(bbox_left)
    image_width = 1.0 * int(image_width)
    width = absolute_width / image_width 
    width = width * 1.0
    return str(width)
def find_height(bbox_top,box_ymax,image_height):
    absolute_height = int(box_ymax) - int(bbox_top)
    image_height = 1.0 * int(image_height)
    height = absolute_height / image_height
    height = height * 1.0
    return str(height)
for f in os.listdir('.'):
    if f != "org.py":
        fname = f
        fname_out = f
		
		
        image_width = 1280
        image_height = 720
        content = []

        with open(fname) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            new_content = []
            for x in content:
                y = x.split(",")
                bbox_left = y[0]
                bbox_left = y[0]
                bbox_top = y[1]
                bbox_width = y[2]
                bbox_height = y[3]
                box_xmax = str(int(y[0]) + int(y[2]))
                box_ymax = str(int(y[1]) + int(y[3]))
                place_0_value = str(1)
                place_1_value = find_x(bbox_left,image_width,box_xmax)
                place_2_value = find_y(image_height,box_ymax,bbox_top)
                place_3_value = find_width(box_xmax,bbox_left,image_width)
                place_4_value = find_height(bbox_top,box_ymax,image_height)
                output = str(place_0_value) + " " + str(place_1_value) + " " + str(place_2_value) + " " + str(place_3_value) + " " + str(place_4_value)
                new_content.append(output)
                with open(fname_out, 'w') as f:
                    f.truncate(0)
                    for item in new_content:
                        f.write("%s\n" % item)
