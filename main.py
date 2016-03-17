import sys
import cv2
import argparse
import os
import conversions.cmy
import conversions.hsv


def convert_model(file_path, used_conversion):
    in_file_path = file_path
    in_image = cv2.imread(in_file_path, cv2.IMREAD_UNCHANGED)

    file_path_with_name, file_extension = os.path.splitext(in_file_path)

    if used_conversion == "rgb2cmy":
        out_image = conversions.cmy.rgb2cmy(in_image)
        cv2.imwrite(file_path_with_name + "RGB2CMY" + file_extension, out_image)
    elif used_conversion == "cmy2rgb":
        out_image = conversions.cmy.cmy2rgb(in_image)
        cv2.imwrite(file_path_with_name + "CMY2RGB" + file_extension, out_image)
    elif used_conversion == "rgb2hsv":
        out_image = conversions.hsv.rgb2hsv(in_image)
        cv2.imwrite(file_path_with_name + "RGB2HSV" + file_extension, out_image)
    else:
        out_image = conversions.hsv.hsv2rgb(in_image)
        cv2.imwrite(file_path_with_name + "HSV2RGB" + file_extension, out_image)


def main():
    parser = argparse.ArgumentParser(description="Color Model Converter")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument("--path", help="Path to image to convert - supported extensions:"
                                              " .bmp, .dib, .jpeg, .jpg, .jpe,"
                                              " .jp2, .png, .webp, .pbm, .pgm,"
                                              " .ppm, .sr, .ras, .tiff, .tif", required=True)
    required_args.add_argument("--convert", help="Type of conversion - available:"
                                                 " rgb2cmy, cmy2rgb,"
                                                 " rgb2hsv, hsv2rgb", required=True)
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
    supported_conversions = ["rgb2cmy", "cmy2rgb", "rgb2hsv", "hsv2rgb"]
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
