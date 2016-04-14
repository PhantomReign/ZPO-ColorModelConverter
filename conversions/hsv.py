import numpy as np
import math


# Source: http://opencv.itseez.com/2.4/modules/imgproc/doc/miscellaneous_transformations.html
#         https://en.wikipedia.org/wiki/HSL_and_HSV
#         http://www.lps.usp.br/hae/apostila/basico/HSI-wikipedia.pdf


def compute_hsv_pixel(R, G, B):
    max_value = max(R, G, B)
    min_value = min(R, G, B)

    if max_value == 0:
        S = 0
    else:
        S = (max_value - min_value) / max_value

    V = max_value
    H = max_value

    if max_value == min_value:
        H = 0
    else:
        if R == max_value:
            H = 60 * (G - B) / (max_value - min_value)
        elif G == max_value:
            H = 120 + 60 * (B - R) / (max_value - min_value)
        elif B == max_value:
            H = 240 + 60 * (R - G) / (max_value - min_value)

    if H < 0:
        H += 360
    H /= 2.

    return H, S, V


def rgb2hsv(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            pixel = compute_hsv_pixel(R, G, B)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0]

    return out_img


def compute_rgb_pixel(H, S, V):
    R = G = B = 0

    i = math.floor(H * 6)
    f = H * 6 - i
    p = V * (1 - S)
    q = V * (1 - f * S)
    t = V * (1 - (1 - f) * S)

    if i % 6 == 0:
        R = V
        G = t
        B = p
    elif i % 6 == 1:
        R = q
        G = V
        B = p
    elif i % 6 == 2:
        R = p
        G = V
        B = t
    elif i % 6 == 3:
        R = p
        G = q
        B = V
    elif i % 6 == 4:
        R = t
        G = p
        B = V
    elif i % 6 == 5:
        R = V
        G = p
        B = q

    return R, G, B


def hsv2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            H = img[col, row][2] / 180.
            S = img[col, row][1] / 255.
            V = img[col, row][0] / 255.

            pixel = compute_rgb_pixel(H, S, V)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img
