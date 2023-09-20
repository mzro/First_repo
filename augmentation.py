# Import the Pillow library
from PIL import Image, ImageEnhance, ImageOps

# Load an image from a file
img = Image.open("ImageInputHere.jpg")

# Flip the image horizontally
img_flip = ImageOps.mirror(img)

# Rotate the image by 90 degrees
img_rotate = img.rotate(-15)
img_rotateR = img.rotate(15)
img_rotateT = img.rotate(-10)
img_rotateL = img.rotate(10)

# Crop the image to a smaller size
img_crop = img.crop((100, 100, 300, 300))

# Resize the image to a larger size
img_resize = img.resize((800, 600))

# Change the brightness of the image
img_bright = ImageEnhance.Brightness(img).enhance(1.5)

# Change the contrast of the image
img_contrast = ImageEnhance.Contrast(img).enhance(2.0)

# Change the color of the image
img_color = ImageEnhance.Color(img).enhance(0.5)

# Save the augmented images to files
img_flip.save("T4_flip.jpg")
img_rotate.save("T4_rotateL.jpg")
img_rotateR.save("T4_rotateR.jpg")
img_rotateT.save("T4_rotateT.jpg")
img_rotateL.save("T4_rotateL.jpg")
img_resize.save("T4_resize.jpg")
img_bright.save("T4_bright.jpg")
img_contrast.save("T4_contrast.jpg")
img_color.save("T4_color.jpg")

# cropping
# img_crop.save("T4_crop.jpg")
