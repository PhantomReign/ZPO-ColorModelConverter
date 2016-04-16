import numpy as np
import conversions.yuv

# Source: http://52.68.174.105:8080/jips/dlibrary/JIPS_v10_no2_paper9.pdf


def compute_pixel(R, G, B):
    Y, U, V = conversions.yuv.compute_yuv_pixel(R, G, B)

    if not (80 < U < 130 and 136 < V < 200 and Y > U):
        Y = U = V = 0

    U -= 128
    V -= 128

    R1, G1, B1 = conversions.yuv.compute_rgb_pixel(Y, U, V)

    if not (R1 > 80 and G1 > 30 and B1 > 15 and abs(R1 - G1) > 15):
        R1 = G1 = B1 = 0

    return R1, G1, B1


def rgb2skin(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2]
            G = img[col, row][1]
            B = img[col, row][0]

            pixel = compute_pixel(R, G, B)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]
    return out_img
