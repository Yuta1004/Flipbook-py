from PIL import Image
import glob

def get_converted_images(path):
    image_A_list = []
    image_B_list = []

    file_list = glob.glob(path)
    file_list = sorted(file_list)

    for fn in file_list:
        image = Image.open(fn)
        image = image.resize((800, 666))
        image_A = image.crop((0, 0, 800, 333))
        image_B = image.crop((0, 333, 800, 666))
        image_A_list.append(image_A)
        image_B_list.append(image_B)

    return image_A_list, image_B_list
