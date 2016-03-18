import cv2
import numpy as np
import math


def rgb2hls(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            max_value = max(R, G, B)
            min_value = min(R, G, B)

            L = (max_value + min_value) / 2

            if max_value == min_value:
                H = 0
                S = 0
            else:
                if L > 0.5:
                    S = (max_value - min_value) / (2 - max_value - min_value)
                else:
                    S = (max_value - min_value) / (max_value + min_value)

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

                if H < 0:
                    H += 1
                elif H > 1:
                    H -= 1

            out_img[col, row][0] = H * 180
            out_img[col, row][1] = L * 255
            out_img[col, row][2] = S * 255

    return out_img


def hue2rgb(v1, v2, vh):
    if vh < 0:
        vh += 1
    elif vh > 1:
        vh -= 1

    if vh * 6 < 1:
        return v1 + (v2 - v1) * 6 * vh
    elif (2 * vh) < 1:
        return v2
    elif (3 * vh) < 2:
        return v1 + (v2 - v1) * ((2 / 3.) - vh) * 6
    else:
        return v1


def hls2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            S = img[col, row][2] / 255.
            L = img[col, row][1] / 255.
            H = img[col, row][0] / 180.

            if S == 0:
                R = L
                G = L
                B = L
            else:
                if L < 0.5:
                    v2 = L * (1. + S)
                else:
                    v2 = (L + S) - (L * S)

                v1 = 2. * L - v2

                H1 = H + (1 / 3.)
                H2 = H - (1 / 3.)

                R = hue2rgb(v1, v2, H1)
                G = hue2rgb(v1, v2, H)
                B = hue2rgb(v1, v2, H2)

            out_img[col, row][0] = B * 255
            out_img[col, row][1] = G * 255
            out_img[col, row][2] = R * 255

    return out_img
