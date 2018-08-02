# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img = Image.open(filename)
    return img

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, filename):
    img.save(filename, "jpeg")

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    list = img.getdata()
    low_int = 182
    medium_int = 364
    high_int = 546
    newpixels = []

    for pixel in list:
        intensity = (pixel[0]+pixel[1]+pixel[2])
        if (intensity < low_int):
            x =(0, 51, 76)
            newpixels.append(x)
        elif (intensity > low_int) and (intensity < medium_int):
            x = (217, 26, 33)
            newpixels.append(x)
        elif (intensity > medium_int) and (intensity < high_int):
            x = (112, 150, 158)
            newpixels.append(x)
        else :
            x = (252, 227, 166)
            newpixels.append(x)

    newimg= Image.new("RGB", img.size)
    newimg.putdata(newpixels)
    return newimg



#
# def obamicon(img):
#     list = img.getdata()
#     low_int = 150
#     medium_int = 300
#     high_int = 546
#     newpixels = []
#
#     for pixel in list:
#         intensity = (pixel[0]+pixel[1]+pixel[2])
#         if (intensity < low_int):
#             x =(255,97,3)
#             newpixels.append(x)
#         elif (intensity > low_int) and (intensity < medium_int):
#             x = (127,255,0)
#             newpixels.append(x)
#         elif (intensity > medium_int) and (intensity < high_int):
#             x = (220,20,60)
#             newpixels.append(x)
#         else :
#             x = (255,185,15)
#             newpixels.append(x)

    newimg= Image.new("RGB", img.size)
    newimg.putdata(newpixels)
    return newimg
