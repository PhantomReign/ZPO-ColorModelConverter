import numpy as np

# Source: https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion


def compute_ycbcr_pixel(R, G, B):

    Y = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
    Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B

    return Y, Cr, Cb


def rgb2ycbcr(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2]
            G = img[col, row][1]
            B = img[col, row][0]

            pixel = compute_ycbcr_pixel(R, G, B)

            out_img[col, row][0] = pixel[0]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[2]

    return out_img


def compute_rgb_pixel(Y, Cb, Cr):
    Cb -= 128
    Cr -= 128

    R = max(0.0, min(255.0, Y + 1.402 * Cr))
    G = max(0.0, min(255.0, Y - 0.34414 * Cb - 0.71414 * Cr))
    B = max(0.0, min(255.0, Y + 1.772 * Cb))

    return R, G, B


def ycbcr2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            Y = img[col, row][0]
            Cr = img[col, row][1]
            Cb = img[col, row][2]

            pixel = compute_rgb_pixel(Y, Cb, Cr)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]

    return out_img
