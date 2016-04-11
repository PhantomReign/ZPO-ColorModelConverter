import numpy as np

# Source: http://www.poynton.com/PDFs/coloureq.pdf


def compute_cmy_pixel(R, G, B):
    C = 1 - R
    M = 1 - G
    Y = 1 - B
    return C, M, Y


def rgb2cmy(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)

    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            pixel = compute_cmy_pixel(R, G, B)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img


def compute_rgb_pixel(C, M, Y):
    R = 1 - C
    G = 1 - M
    B = 1 - Y
    return R, G, B


def cmy2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)

    for col in range(cols):
        for row in range(rows):
            C = img[col, row][2] / 255.
            M = img[col, row][1] / 255.
            Y = img[col, row][0] / 255.

            pixel = compute_rgb_pixel(C, M, Y)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img
