import numpy as np

# SOURCE: http://opencv.itseez.com/2.4/modules/imgproc/doc/miscellaneous_transformations.html


def compute_xyz_pixel(R, G, B):

    X = R * 0.412453 + G * 0.357580 + B * 0.180423
    Y = R * 0.212671 + G * 0.715160 + B * 0.072169
    Z = R * 0.019334 + G * 0.119193 + B * 0.950227

    if Z > 1.0:
        Z = 1.0

    return X, Y, Z


def rgb2xyz(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            pixel = compute_xyz_pixel(R, G, B)

            out_img[col, row][0] = pixel[0] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[2] * 255

    return out_img


def compute_rgb_pixel(X, Y, Z):

    R = 3.240479 * X - 1.53715 * Y - 0.498535 * Z
    G = -0.969256 * X + 1.875991 * Y + 0.041556 * Z
    B = 0.055648 * X - 0.204043 * Y + 1.057311 * Z

    if R < 0:
        R = 0
    elif R > 255:
        R = 255

    if G < 0:
        G = 0
    elif G > 255:
        G = 255

    if B < 0:
        B = 0
    elif B > 255:
        B = 255

    return R, G, B


def xyz2rgb(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            X = img[col, row][0]
            Y = img[col, row][1]
            Z = img[col, row][2]

            pixel = compute_rgb_pixel(X, Y, Z)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]

    return out_img
