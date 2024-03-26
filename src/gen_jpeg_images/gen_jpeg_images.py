# -*- coding: utf-8 -*-
"""gen_images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpabFTtkNxNgP3MVK33SCV2Na26N-2QL
"""

#!/Ausr/bin/env python
# -------------------------------------------------------------------------------
# 1. implement this python file, for future research
# 2. Explore compression ratio for different patterns (synthetic)
# -------------------------------------------------------------------------------
# 3. check the compression ratio for real photos (100)
#    - read the photo (compressed), check the size of the image (decompressed)
# -------------------------------------------------------------------------------
# if possible, use argparse, python gen_images.py --num_images 1000 --dim 224 224


# num_images=100
# dim1 = 224
# dim2 = 224

# for i in range(1000):
#     fout = f"image-{i}.png"
#     pattern = np.random.randint(1, 5)
#     gen_image(dim1, dim2, pattern, fout)

import argparse

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# PATTERN:
#    0 - ALL_ZERO
#    1 - ALL_ONE
#    2 - STRIPE
#    3 - CHECKERBOARD
#    4 - RANDOM

def gen_image(dim1, dim2, pattern):
    # compression (True of False)
    # https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html
    # 1 - generate 2d random matrix
    # 2 - save the matrix to a file
    # Different pattern (exploration)
    #   a. all zero
    #   b.

    '''
    generate image of dimension (dim1, dim2), and save it to fout ("image1.png")
    random images
    '''
    if (pattern == 0):
      arr = np.zeros((dim1, dim2), dtype='uint8')
    elif (pattern == 1):
      arr = np.ones((dim1, dim2), dtype='uint8')
    elif (pattern == 2):
      arr = np.arange(dim1, dtype='uint8')[:, np.newaxis]
      arr = np.tile(arr, (1, dim2))
    elif (pattern == 3):
      arr = np.zeros((dim1, dim2), dtype='uint8')
      arr[1::2, ::2] = 1 # Set odd rows, even columns to 1
      arr[::2, 1::2] = 1 # Set even rows, odd columns to 1
    else:
      arr = np.random.randint(256, size=(dim1, dim2), dtype='uint8')

    return arr

def save_image(image, filename):
#    plt.imshow(image, interpolation='nearest')
#    plt.axis('off')  # Turn off axis
#    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    img = Image.fromarray(image)
    img.save(filename)

def plot_image(image):
    plt.imshow(image, interpolation='nearest')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Generate and save images with different patterns.')
    parser.add_argument('--num_images', type=int, required=True, help='Number of images to generate')
    parser.add_argument('--dim1', type=int, required=True, help='Dimension 1 of the images')
    parser.add_argument('--dim2', type=int, required=True, help='Dimension 2 of the images')

    args = parser.parse_args()

    pattern = int(input("Enter the pattern: "))
    for i in range(args.num_images):
        image = gen_image(args.dim1, args.dim2, pattern)

        fout_jpeg = f"image-{i}.jpeg"
        save_image(image, fout_jpeg)

        if i < 5:  # Plot the first 5 images for visualization
            plot_image(image)

if __name__ == '__main__':
    main()
