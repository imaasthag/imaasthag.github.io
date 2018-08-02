import filters

def main():
    filename = input("Enter file name: ")

    im = filters.load_img(filename)


    newimage = filters.obamicon(im)
    filters.show_img(newimage)
    filters.save_img(newimage, "newfilename.jpg")



if __name__ == '__main__':
    main()
