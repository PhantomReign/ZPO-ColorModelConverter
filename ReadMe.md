********************************************************************************
*           ___        _                                   _        _          *
*          / __\ ___  | |  ___   _ __    /\/\    ___    __| |  ___ | |         *
*         / /   / _ \ | | / _ \ | '__|  /    \  / _ \  / _` | / _ \| |         *
*        / /___| (_) || || (_) || |    / /\/\ \| (_) || (_| ||  __/| |         *
*        \____/ \___/ |_| \___/ |_|    \/    \/ \___/  \__,_| \___||_|         *
*               ___                                _                           *
*              / __\ ___   _ __ __   __ ___  _ __ | |_  ___  _ __              *
*             / /   / _ \ | '_ \\ \ / // _ \| '__|| __|/ _ \| '__|             *
*            / /___| (_) || | | |\ V /|  __/| |   | |_|  __/| |                *
*            \____/ \___/ |_| |_| \_/  \___||_|    \__|\___||_|                *
*                                                                              *
*                               ZPO Project 2016                               *
********************************************************************************
*   Created by Matúš Turic (xturic01) and Peter Cilip (xcilip00) at VUT FIT    *
********************************************************************************

description: Application converts image to selected model based on conversion 
             type. All converted files will be stored in source file directory.

usage: python cmc.py [-h] -p PATH -c CONVERSION

optional arguments:
  -h, --help     Show help message and exit

required arguments:
  -p PATH        Path to image file - supported extensions: .bmp, .dib, .jpeg,
                 .jpg, .jpe, .jp2, .png, .webp, .pbm, .pgm, .ppm, .sr, .ras,
                 .tiff, .tif
  -c CONVERSION  Type of conversion - available: rgb2cmy, cmy2rgb, rgb2hsv,
                 hsv2rgb, rgb2hsl, hsl2rgb, rgb2ycbcr, ycbcr2rgb, rgb2xyz,
                 xyz2rgb, rgb2yuv, yuv2rgb, rgb2skin, rgb2grey, rgb2p-nopia,
                 rgb2d-nopia, rgb2t-nopia, all
