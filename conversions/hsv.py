import cv2
import numpy as np
import math


# used Foley and VanDam algorithm
def rgb2hsv(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            maxValue = max(R, G, B)
            minValue = min(R, G, B)

            if maxValue == 0:
                S = 0
            else:
                S = (maxValue - minValue) / maxValue

            V = maxValue
            H = maxValue

            if maxValue == minValue:
                H = 0
            else:
                if R == maxValue:
                    if G < B:
                        H = (G - B) / (maxValue - minValue) + 6
                    else:
                        H = (G - B) / (maxValue - minValue) + 0
                elif G == maxValue:
                    H = (B - R) / (maxValue - minValue) + 2
                elif B == maxValue:
                    H = (R - G) / (maxValue - minValue) + 4

                H /= 6.

            out_img[col, row][0] = H * 180
            out_img[col, row][1] = S * 255
            out_img[col, row][2] = V * 255

    return out_img


def hsv2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            V = img[col, row][2] / 255.
            S = img[col, row][1] / 255.
            H = img[col, row][0] / 180.

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

            out_img[col, row][0] = B * 255
            out_img[col, row][1] = G * 255
            out_img[col, row][2] = R * 255

    return out_img
