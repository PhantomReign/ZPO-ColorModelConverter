import numpy as np
import math


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
            if G < B:
                H = (G - B) / (max_value - min_value) + 6
            else:
                H = (G - B) / (max_value - min_value) + 0
        elif G == max_value:
            H = (B - R) / (max_value - min_value) + 2
        elif B == max_value:
            H = (R - G) / (max_value - min_value) + 4

        H /= 6.

    return H, S, V


# used Foley and VanDam algorithm
def rgb2hsv(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            pixel = compute_hsv_pixel(R, G, B)

            out_img[col, row][0] = pixel[0] * 180
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[2] * 255

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
            V = img[col, row][2] / 255.
            S = img[col, row][1] / 255.
            H = img[col, row][0] / 180.

            pixel = compute_rgb_pixel(H, S, V)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img
