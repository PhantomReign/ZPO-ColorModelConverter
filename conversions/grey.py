import numpy as np

# Source: http://opencv.itseez.com/2.4/modules/imgproc/doc/miscellaneous_transformations.html


def compute_grey_pixel(R, G, B):
    GS = R * 0.299 + G * 0.587 + B * 0.114
    GSR = round(GS)
    return GSR, GSR, GSR


def rgb2grey(img):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.uint8)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2]
            G = img[col, row][1]
            B = img[col, row][0]

            pixel = compute_grey_pixel(R, G, B)

            out_img[col, row][0] = pixel[2]
            out_img[col, row][1] = pixel[1]
            out_img[col, row][2] = pixel[0]

    return out_img