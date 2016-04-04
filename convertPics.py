import main
import shutil
import os


def move_file(source, destination):
    if os.path.exists(destination):
        if os.path.isdir(destination):
            shutil.copy(source, destination)
            os.remove(source)
        else:
            os.remove(destination)


# skin segmentation
main.convert_model("images/anne.jpg", "rgb2skin")
move_file("images/anneRGB2SKIN.jpg", "converted")


main.convert_model("images/leo.png", "rgb2skin")
move_file("images/leoRGB2SKIN.png", "converted")

main.convert_model("images/lawrence.png", "rgb2skin")
move_file("images/lawrenceRGB2SKIN.png", "converted")
