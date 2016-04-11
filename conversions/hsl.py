import numpy as np

# Source: http://axonflux.com/handy-rgb-to-hsl-and-rgb-to-hsv-color-model-c
#         https://en.wikipedia.org/wiki/HSL_and_HSV
#         http://opencv.itseez.com/2.4/modules/imgproc/doc/miscellaneous_transformations.html


def compute_hsl_pixel(R, G, B):
    max_value = max(R, G, B)
    min_value = min(R, G, B)
    H = S = 0
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

    return H, S, L


def rgb2hsl(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            pixel = compute_hsl_pixel(R, G, B)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 180

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


def compute_rgb_pixel(H, S, L):
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

    return R, G, B


def hsl2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            H = img[col, row][2] / 180.
            S = img[col, row][1] / 255.
            L = img[col, row][0] / 255.

            pixel = compute_rgb_pixel(H, S, L)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img
