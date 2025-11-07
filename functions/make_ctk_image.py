import os
from PIL import Image
from customtkinter import CTkImage

# This function takes any imported image and converts it to a CTK Image to be used by the application.

# This is the directory where images are stored. It combines the directory with the image folder.
ImageDirectory = os.path.join(os.getcwd(), "images")


def make_ctk_image(image_name, image_size):
    # Open the image using PIL.
    image = Image.open(os.path.join(ImageDirectory, image_name))
    # Convert image with the defined size into a CTk image.
    clean_image = CTkImage(dark_image=image, size=image_size)

    # Return clean image for use in the application.
    return clean_image
