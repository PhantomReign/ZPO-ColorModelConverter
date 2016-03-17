import cv2
import numpy as np


def rgb2cmy(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)

    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            C = 1 - R
            M = 1 - G
            Y = 1 - B

            out_img[col, row][0] = Y * 255
            out_img[col, row][1] = M * 255
            out_img[col, row][2] = C * 255

    return out_img


def cmy2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)

    for col in range(cols):
        for row in range(rows):
            C = img[col, row][2] / 255.
            M = img[col, row][1] / 255.
            Y = img[col, row][0] / 255.

            R = 1 - C
            G = 1 - M
            B = 1 - Y

            out_img[col, row][0] = B * 255
            out_img[col, row][1] = G * 255
            out_img[col, row][2] = R * 255

    return out_img
