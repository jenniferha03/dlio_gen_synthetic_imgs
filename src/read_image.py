import os
import sys

import numpy as np
import pandas as pd
from numpy import asarray
from PIL import Image


def count_occurences(matrix):
    occurences = {}
    for row in matrix:
        for num in row:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1
    return occurences


def read_image(filename):
    # Open the image file
    image = Image.open(filename)
    numpydata = asarray(image)

    # Display some information about the image
    print("Image format:", image.format)
    print("Image mode:", image.mode)
    print("Image size:", image.size)

    # Get the file size in bytes
    file_size = os.path.getsize(filename)
    print("File size:", file_size, "bytes")
    print(numpydata)
    result = count_occurences(numpydata)
    # Sort the keys
    sorted_result = sorted(result.keys())

    df = pd.DataFrame(sorted_result)
    df.to_csv(f"{filename}.csv")

    # Print the dictionary in order
    print({key: result[key] for key in sorted_result})

    #    # Transform to pixels
    #    pixels = image.img_to_array(filename)

    # Show the image
    image.show()


def main(filename):
    # Check if the file is an image or .npz file
    if filename.endswith(".npz"):
        # Load the .npz file
        data = np.load(filename)

        # Print keys to identify the correct key
        print("Keys in the .npz file:", list(data.keys()))

        # Close the .npz file
        data.close()
    else:
        # Read the image file
        read_image(filename)


if __name__ == "__main__":
    # Check if filename argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3.10 script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
