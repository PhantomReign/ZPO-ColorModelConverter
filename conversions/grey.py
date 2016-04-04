import numpy as np


def compute_grey_pixel(R, G, B):
    GS = R * 0.299 + G * 0.587 + B * 0.114
    return GS, GS, GS


def rgb2grey(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2]
            G = img[col, row][1]
            B = img[col, row][0]

            pixel = compute_grey_pixel(R, G, B)

            out_img[col, row][0] = pixel[0]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[2]

    return out_img