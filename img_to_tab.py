import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def convert_img_to_tab(name_of_image: str):
    image_np = mpimg.imread(name_of_image)
    print(type(image_np))