import numpy as np


# SOURCE: http://www.daltonize.org/

def compute_lms_pixel(R, G, B):
    L = (17.8824 * R) + (43.5161 * G) + (4.11935 * B)
    M = (3.45565 * R) + (27.1554 * G) + (3.86714 * B)
    S = (0.0299566 * R) + (0.184309 * G) + (1.46709 * B)
    return L, M, S


def compute_rgb_pixel(L, M, S):
    R = (0.0809444479 * L) + (-0.130504409 * M) + (0.116721066 * S)
    G = (-0.0102485335 * L) + (0.0540193266 * M) + (-0.113614708 * S)
    B = (-0.000365296938 * L) + (-0.00412161469 * M) + (0.693511405 * S)
    return R, G, B


def compute_protanopia_pixel(R, G, B):
    L, M, S = compute_lms_pixel(R, G, B)

    Lp = 2.02344 * M - 2.52581 * S
    Mp = M
    Sp = S

    Rp, Gp, Bp = compute_rgb_pixel(Lp, Mp, Sp)

    if Rp < 0:
        Rp = 0
    elif Rp > 1:
        Rp = 1

    if Gp < 0:
        Gp = 0
    elif Gp > 1:
        Gp = 1

    if Bp < 0:
        Bp = 0
    elif Bp > 1:
        Bp = 1

    return Rp, Gp, Bp


def compute_deuteranopia_pixel(R, G, B):
    L, M, S = compute_lms_pixel(R, G, B)

    Ld = L
    Md = 0.494207 * L + 1.24827 * S
    Sd = S

    Rd, Gd, Bd = compute_rgb_pixel(Ld, Md, Sd)

    if Rd < 0:
        Rd = 0
    elif Rd > 1:
        Rd = 1

    if Gd < 0:
        Gd = 0
    elif Gd > 1:
        Gd = 1

    if Bd < 0:
        Bd = 0
    elif Bd > 1:
        Bd = 1

    return Rd, Gd, Bd


def compute_tritanopia_pixel(R, G, B):
    L, M, S = compute_lms_pixel(R, G, B)

    Lt = L
    Mt = M
    St = -0.012245 * L + 0.072035 * M

    Rt, Gt, Bt = compute_rgb_pixel(Lt, Mt, St)

    if Rt < 0:
        Rt = 0
    elif Rt > 1:
        Rt = 1

    if Gt < 0:
        Gt = 0
    elif Gt > 1:
        Gt = 1

    if Bt < 0:
        Bt = 0
    elif Bt > 1:
        Bt = 1

    return Rt, Gt, Bt


def rgb2deficit(img, deficit):
    cols, rows, channels = img.shape
    out_img = np.zeros((cols, rows, 3), np.double)
    for col in range(cols):
        for row in range(rows):
            R = img[col, row][2] / 255.
            G = img[col, row][1] / 255.
            B = img[col, row][0] / 255.

            if deficit == "rgb2p-nope":
                pixel = compute_protanopia_pixel(R, G, B)
            elif deficit == "rgb2d-nope":
                pixel = compute_deuteranopia_pixel(R, G, B)
            else:
                pixel = compute_tritanopia_pixel(R, G, B)

            out_img[col, row][0] = pixel[2] * 255
            out_img[col, row][1] = pixel[1] * 255
            out_img[col, row][2] = pixel[0] * 255

    return out_img
