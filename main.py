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


def save_img(image, path, conversion, extension):
    cv2.imwrite(path + conversion + extension, image)


def convert_model(file_path, used_conversion):
    in_file_path = file_path
    in_image = cv2.imread(in_file_path, cv2.IMREAD_UNCHANGED)

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


def main():
    parser = argparse.ArgumentParser(description="Color Model Converter")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument("--path", help="Path to image to convert - supported extensions:"
                                              " .bmp, .dib, .jpeg, .jpg, .jpe,"
                                              " .jp2, .png, .webp, .pbm, .pgm,"
                                              " .ppm, .sr, .ras, .tiff, .tif", required=True)
    required_args.add_argument("--convert", help="Type of conversion - available:"
                                                 " rgb2cmy, cmy2rgb,"
                                                 " rgb2hsv, hsv2rgb"
                                                 " rgb2hsl, hsl2rgb"
                                                 " rgb2ycbcr, ycbcr2rgb"
                                                 " rgb2xyz, xyz2rgb"
                                                 " rgb2yuv, yuv2rgb"
                                                 " rgb2skin, rgb2grey"
                                                 " rgb2p-nopia, rgb2d-nopia"
                                                 " rgb2t-nopia", required=True)
    args = parser.parse_args()

    if not os.path.isfile(args.path):
        sys.stderr.write('error: File does not exist\n')
        sys.exit(-1)

    file_extension = os.path.splitext(args.path)[1]
    used_conversion = args.convert

    extension_error = True
    supported_extensions = [".bmp", ".dib", ".jpeg", ".jpg", ".jpe",
                            ".jp2", ".png", ".webp", ".pbm", ".pgm",
                            ".ppm", ".sr", ".ras", ".tiff", ".tif"]

    for extension in supported_extensions:
        if extension == file_extension:
            extension_error = False

    if extension_error:
        sys.stderr.write('error: File is not supported\n'
                         'Use [-h] for help\n')
        sys.exit(-2)

    conversion_error = True
    supported_conversions = ["rgb2cmy", "cmy2rgb", "rgb2hsv", "hsv2rgb", "rgb2hsl", "hsl2rgb",
                             "rgb2ycbcr", "ycbcr2rgb", "rgb2xyz", "xyz2rgb", "rgb2yuv", "yuv2rgb",
                             "rgb2skin", "rgb2grey", "rgb2p-nopia", "rgb2d-nopia", "rgb2t-nopia"]
    for conversion in supported_conversions:
        if used_conversion == conversion:
            conversion_error = False

    if conversion_error:
        sys.stderr.write('error: Conversion is not supported\n'
                         'Use [-h] for help\n')
        sys.exit(-3)

    convert_model(args.path, used_conversion)


if __name__ == '__main__':
    main()
