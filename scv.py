import cv2

def img_load(img_path):
    """
    Wrapper for cv2.imread, because we don't want the kids to have to access OpenCV directly.
    """
    return cv2.imread(img_path, -1)  # Load the image with any alphas

def draw(l_img, s_img, x_offset, y_offset, width, height):
    """
    Draws s_image on top of l_image starting at an x and y offset from the top left corner of the image, and with the
    given width and height.
    """
    s_img = cv2.resize(s_img, (width, height), interpolation = cv2.INTER_AREA)  # Resize overlay image

    # This Terrible Code was Copy Pasted Code from. OpenCV makes this really annoying but it works.:
    # http://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
    for c in range(0,3):
        l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] = s_img[:,:,c] * (s_img[:,:,3]/255.0) +  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] * (1.0 - s_img[:,:,3]/255.0)

    return l_img  # Return the drawn over background image

def show_image(img):
    cv2.imshow('Display', img)
    cv2.waitKey(0)

def get_height(img):
    return img.shape[0]

def get_width(img):
    return img.shape[1]
