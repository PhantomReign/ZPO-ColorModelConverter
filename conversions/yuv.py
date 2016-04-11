import numpy as np

# Source: http://www.poynton.com/PDFs/coloureq.pdf


def compute_yuv_pixel(R, G, B):

    Y = R * 0.299 + G * 0.587 + B * 0.114
    U = R * -0.147 + G * -0.289 + B * 0.436 + 128
    V = R * 0.615 + G * -0.515 + B * -0.100 + 128

    return round(Y), round(U), round(V)


def rgb2yuv(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2]
            G = img[col, row][1]
            B = img[col, row][0]

            pixel = compute_yuv_pixel(R, G, B)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]

    return out_img


def compute_rgb_pixel(Y, U, V):

    R = Y + 1.140 * V
    G = Y - 0.396 * U - 0.581 * V
    B = Y + 2.029 * U

    if R < 0:
        R = 0
    if G < 0:
        G = 0
    if B < 0:
        B = 0

    if R > 255:
        R = 255
    if G > 255:
        G = 255
    if B > 255:
        B = 255

    return round(R), round(G), round(B)


def yuv2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            Y = img[col, row][2]
            U = img[col, row][1]
            V = img[col, row][0]

            U -= 128
            V -= 128

            pixel = compute_rgb_pixel(Y, U, V)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]

    return out_img
