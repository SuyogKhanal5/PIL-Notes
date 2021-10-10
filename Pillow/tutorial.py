from PIL import Image

image1 = Image.open(r"C:\Users\suyog\Python Projects\Pillow\OP.jpg")

# Since they are in the same folder, should be able to just type "OP.JPG" and have it open, but that didn't work, so
# I had to paste the whole path in here, and also convert to a raw string, when neither should be necessary
# But if it works it works i guess

# Figured it out, it is looking in the Python Projects folder instead of the Pillow folder for some reason.
# It is also saving images there as well, so I will have to specify the path for that as well

# image1.show() Opens the file in default application to open img files
 
# image1.save(r"C:\Users\suyog\Python Projects\Pillow\OP2.png") Save the file as any image type

image1.rotate(90).save(r"C:\Users\suyog\Python Projects\Pillow\OP2.png") # Rotate the file, and you can save on the same line

image1.rotate(90).convert(mode = 'L').save(r"C:\Users\suyog\Python Projects\Pillow\OP2_Edit.png")
