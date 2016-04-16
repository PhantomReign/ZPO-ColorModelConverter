import sys
import cv2
import argparse
import os
import conversions.cmy
import conversions.hsv
import conversions.hsl
import conversions.ycbcr
import conversions.xyz
import conversions.yuv
import conversions.skin_segmentation
import conversions.grey
import conversions.color_deficit


def file_choices(parser, choices, image_file):
    extension = os.path.splitext(image_file)[1]
    if extension not in choices:
        parser.error("argument --path: invalid choice: {0} choose from {1})".format(extension, ", ".join(
            "'" + item + "'" for item in choices)))
    return image_file


def save_img(image, path, conversion, extension):
    try:
        cv2.imwrite(path + conversion + extension, image)
    except cv2.error:
        sys.stderr.write("Please try to convert the image to another format.\n")
        exit(-3)


def load_img(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        sys.stderr.write("error: OpenCV can't load this image. Try to convert it.\n")
        sys.exit(-2)
    if len(image.shape) < 3:
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    return image


def convert_model(file_path, used_conversion):
    in_file_path = file_path
    in_image = load_img(in_file_path)

    file_path_with_name, file_extension = os.path.splitext(in_file_path)

    if used_conversion == "rgb2cmy":
        out_image = conversions.cmy.rgb2cmy(in_image)
        save_img(out_image, file_path_with_name, "RGB2CMY", file_extension)
    elif used_conversion == "cmy2rgb":
        out_image = conversions.cmy.cmy2rgb(in_image)
        save_img(out_image, file_path_with_name, "CMY2RGB", file_extension)
    elif used_conversion == "rgb2hsv":
        out_image = conversions.hsv.rgb2hsv(in_image)
        save_img(out_image, file_path_with_name, "RGB2HSV", file_extension)
    elif used_conversion == "hsv2rgb":
        out_image = conversions.hsv.hsv2rgb(in_image)
        save_img(out_image, file_path_with_name, "HSV2RGB", file_extension)
    elif used_conversion == "rgb2hsl":
        out_image = conversions.hsl.rgb2hsl(in_image)
        save_img(out_image, file_path_with_name, "RGB2HSL", file_extension)
    elif used_conversion == "hsl2rgb":
        out_image = conversions.hsl.hsl2rgb(in_image)
        save_img(out_image, file_path_with_name, "HSL2RGB", file_extension)
    elif used_conversion == "rgb2ycbcr":
        out_image = conversions.ycbcr.rgb2ycbcr(in_image)
        save_img(out_image, file_path_with_name, "RGB2YCBCR", file_extension)
    elif used_conversion == "ycbcr2rgb":
        out_image = conversions.ycbcr.ycbcr2rgb(in_image)
        save_img(out_image, file_path_with_name, "YCBCR2RGB", file_extension)
    elif used_conversion == "rgb2xyz":
        out_image = conversions.xyz.rgb2xyz(in_image)
        save_img(out_image, file_path_with_name, "RGB2XYZ", file_extension)
    elif used_conversion == "xyz2rgb":
        out_image = conversions.xyz.xyz2rgb(in_image)
        save_img(out_image, file_path_with_name, "XYZ2RGB", file_extension)
    elif used_conversion == "rgb2yuv":
        out_image = conversions.yuv.rgb2yuv(in_image)
        save_img(out_image, file_path_with_name, "RGB2YUV", file_extension)
    elif used_conversion == "yuv2rgb":
        out_image = conversions.yuv.yuv2rgb(in_image)
        save_img(out_image, file_path_with_name, "YUV2RGB", file_extension)
    elif used_conversion == "rgb2skin":
        out_image = conversions.skin_segmentation.rgb2skin(in_image)
        save_img(out_image, file_path_with_name, "RGB2SKIN", file_extension)
    elif used_conversion == "rgb2grey":
        out_image = conversions.grey.rgb2grey(in_image)
        save_img(out_image, file_path_with_name, "RGB2GREY", file_extension)
    elif used_conversion == "rgb2p-nopia":
        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2p-nopia")
        save_img(out_image, file_path_with_name, "RGB2P-NOPIA", file_extension)
    elif used_conversion == "rgb2d-nopia":
        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2d-nopia")
        save_img(out_image, file_path_with_name, "RGB2D-NOPIA", file_extension)
    elif used_conversion == "rgb2t-nopia":
        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2t-nopia")
        save_img(out_image, file_path_with_name, "RGB2T-NOPIA", file_extension)
    elif used_conversion == "all":
        out_image = conversions.cmy.rgb2cmy(in_image)
        save_img(out_image, file_path_with_name, "RGB2CMY", file_extension)

        out_image = conversions.hsv.rgb2hsv(in_image)
        save_img(out_image, file_path_with_name, "RGB2HSV", file_extension)

        out_image = conversions.hsl.rgb2hsl(in_image)
        save_img(out_image, file_path_with_name, "RGB2HSL", file_extension)

        out_image = conversions.ycbcr.rgb2ycbcr(in_image)
        save_img(out_image, file_path_with_name, "RGB2YCBCR", file_extension)

        out_image = conversions.xyz.rgb2xyz(in_image)
        save_img(out_image, file_path_with_name, "RGB2XYZ", file_extension)

        out_image = conversions.yuv.rgb2yuv(in_image)
        save_img(out_image, file_path_with_name, "RGB2YUV", file_extension)

        out_image = conversions.skin_segmentation.rgb2skin(in_image)
        save_img(out_image, file_path_with_name, "RGB2SKIN", file_extension)

        out_image = conversions.grey.rgb2grey(in_image)
        save_img(out_image, file_path_with_name, "RGB2GREY", file_extension)

        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2p-nopia")
        save_img(out_image, file_path_with_name, "RGB2P-NOPIA", file_extension)

        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2d-nopia")
        save_img(out_image, file_path_with_name, "RGB2D-NOPIA", file_extension)

        out_image = conversions.color_deficit.rgb2deficit(in_image, "rgb2t-nopia")
        save_img(out_image, file_path_with_name, "RGB2T-NOPIA", file_extension)
    else:
        sys.stderr.write('error: unsupported conversion\n')
        sys.exit(-2)


def main():
    parser = argparse.ArgumentParser(description="Color Model Converter - ZPO Project 2016",
                                     epilog="All converted files will be stored in source file directory")
    supported_extensions = [".bmp", ".dib", ".jpeg", ".jpg", ".jpe",
                            ".jp2", ".png", ".webp", ".pbm", ".pgm",
                            ".ppm", ".sr", ".ras", ".tiff", ".tif"]
    supported_conversions = ["rgb2cmy", "cmy2rgb", "rgb2hsv", "hsv2rgb", "rgb2hsl", "hsl2rgb",
                             "rgb2ycbcr", "ycbcr2rgb", "rgb2xyz", "xyz2rgb", "rgb2yuv", "yuv2rgb",
                             "rgb2skin", "rgb2grey", "rgb2p-nopia", "rgb2d-nopia", "rgb2t-nopia", "all"]
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument("-p",
                               help="path to image file - supported extensions: " + ", ".join(supported_extensions),
                               required=True,
                               type=lambda f: file_choices(parser, supported_extensions, f),
                               metavar="PATH")
    required_args.add_argument("-c",
                               help="type of conversion - available: " + ", ".join(supported_conversions),
                               required=True,
                               choices=supported_conversions,
                               metavar="CONVERSION")
    args = parser.parse_args()

    if not os.path.isfile(args.p):
        sys.stderr.write('error: file does not exist\n')
        sys.exit(-1)

    convert_model(args.p, args.c)


if __name__ == '__main__':
    main()
