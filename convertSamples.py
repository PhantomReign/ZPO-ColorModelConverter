import cmc
import shutil
import os
import argparse
import sys

# test file - used for demonstration


def move_file(source, destination):
    if os.path.exists(destination):
        if os.path.isdir(destination):
            shutil.copy(source, destination)
            os.remove(source)
        else:
            os.remove(destination)


def cmy():
    cmc.convert_model("images/leo.png", "rgb2cmy")
    move_file("images/leoRGB2CMY.png", "converted")
    cmc.convert_model("converted/leoRGB2CMY.png", "cmy2rgb")


def grey():
    cmc.convert_model("images/leo.png", "rgb2grey")
    move_file("images/leoRGB2GREY.png", "converted")


def hsl():
    cmc.convert_model("images/leo.png", "rgb2hsl")
    move_file("images/leoRGB2HSL.png", "converted")
    cmc.convert_model("converted/leoRGB2HSL.png", "hsl2rgb")


def hsv():
    cmc.convert_model("images/leo.png", "rgb2hsv")
    move_file("images/leoRGB2HSV.png", "converted")
    cmc.convert_model("converted/leoRGB2HSV.png", "hsv2rgb")


def xyz():
    cmc.convert_model("images/leo.png", "rgb2xyz")
    move_file("images/leoRGB2XYZ.png", "converted")
    cmc.convert_model("converted/leoRGB2XYZ.png", "xyz2rgb")


def ycbcr():
    cmc.convert_model("images/leo.png", "rgb2ycbcr")
    move_file("images/leoRGB2YCBCR.png", "converted")
    cmc.convert_model("converted/leoRGB2YCBCR.png", "ycbcr2rgb")


def yuv():
    cmc.convert_model("images/leo.png", "rgb2yuv")
    move_file("images/leoRGB2YUV.png", "converted")
    cmc.convert_model("converted/leoRGB2YUV.png", "yuv2rgb")


def skin():
    cmc.convert_model("images/anne.jpg", "rgb2skin")
    move_file("images/anneRGB2SKIN.jpg", "converted")

    cmc.convert_model("images/leo.png", "rgb2skin")
    move_file("images/leoRGB2SKIN.png", "converted")

    cmc.convert_model("images/lawrence.png", "rgb2skin")
    move_file("images/lawrenceRGB2SKIN.png", "converted")


def deficit():
    cmc.convert_model("images/metro.jpg", "rgb2p-nopia")
    move_file("images/metroRGB2P-NOPIA.jpg", "converted")
    cmc.convert_model("images/metro.jpg", "rgb2d-nopia")
    move_file("images/metroRGB2D-NOPIA.jpg", "converted")
    cmc.convert_model("images/metro.jpg", "rgb2t-nopia")
    move_file("images/metroRGB2T-NOPIA.jpg", "converted")

    cmc.convert_model("images/paprika.jpg", "rgb2p-nopia")
    move_file("images/paprikaRGB2P-NOPIA.jpg", "converted")
    cmc.convert_model("images/paprika.jpg", "rgb2d-nopia")
    move_file("images/paprikaRGB2D-NOPIA.jpg", "converted")
    cmc.convert_model("images/paprika.jpg", "rgb2t-nopia")
    move_file("images/paprikaRGB2T-NOPIA.jpg", "converted")


# ----------------------------------------------- MAIN -----------------------------------------------------
parser = argparse.ArgumentParser(description="CMC - run samples")
required_args = parser.add_argument_group('required arguments')
required_args.add_argument("--model", help="Convert images to model - supported parameters:"
                                           " all, cmy, deficit, grey, hsl,"
                                           " hsv, skin, xyz, ycbcr, yuv", required=True)

args = parser.parse_args()

used_model = args.model
model_error = True
supported_models = ["all", "cmy", "deficit", "grey", "hsl",
                    "hsv", "skin", "xyz", "ycbcr", "yuv"]

for model in supported_models:
    if model == used_model:
        model_error = False

if model_error:
    sys.stderr.write('error: Conversion is not supported\n'
                     'Use [-h] for help\n')
    sys.exit(-2)


if used_model == "cmy":
    cmy()
elif used_model == "grey":
    grey()
elif used_model == "hsl":
    hsl()
elif used_model == "hsv":
    hsv()
elif used_model == "xyz":
    xyz()
elif used_model == "ycbcr":
    ycbcr()
elif used_model == "yuv":
    yuv()
elif used_model == "skin":
    skin()
elif used_model == "deficit":
    deficit()
else:
    cmy()
    grey()
    hsl()
    hsv()
    xyz()
    ycbcr()
    yuv()
    skin()
    deficit()
