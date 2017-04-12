from scv import *

mode = 1

# SUPER CHALLENGE # 1 ANSWER
if mode == 0:    
    img = img_load('parlor.png')
    cone = img_load('cone.png')
    cream = img_load('greencircle.png')
    img = draw(img, cream, get_width(img)/2 - 50, get_height(img)/2 - 65, 100, 100)
    img = draw(img, cone, get_width(img)/2 - 50, get_height(img)/2, 100, 200)
    show_image(img)
    
# MOUTH DETECT AND DRAW CHALLENGE
elif mode == 1:
    original = img_load('face_detect.png')  # Load the original image
    mouths = find_mouths(original)  # Find the mouths
    if len(mouths) != 0: # If there are mouths
        x, y, width, height = mouths[-1]  # Get best match for mouth
        original = draw(original, img_load('greencircle.png'), x, y, width, height)
    show_image(original)

# MUSTACHE FINAL CHALLENGE ANSWER 
elif mode == 2:
    stache = img_load('stache.png')  # Load the stache
    while True:
        original = get_camera_image()  # Load the original image
        mouths = find_mouths(original)  # Find the mouths
        
        if len(mouths) != 0: # If there are mouths
            x, y, width, height = mouths[-1]  # Get best match for mouth
            original = draw(original, stache, x, int(y-height/3.5), width, int(height/1.2))
        
        show_image(original)

