from scv import *

# SUPER CHALLENGE # 1 ANSWER
img = img_load('parlor.png')
cone = img_load('cone.png')
cream = img_load('greencircle.png')
img = draw(img, cream, get_width(img)/2 - 50, get_height(img)/2 - 65, 100, 100)
img = draw(img, cone, get_width(img)/2 - 50, get_height(img)/2, 100, 200)
show_image(img)



