from PIL import Image

def file_is_image(file_path):
    # Check if a file is an image (using Pillow)
    try:
        Image.open(file_path)
        return True
    except (IOError, OSError):
        return False

def compare_images(file, image_path1, image_path2):

    # Compare images pixel by pixel
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    if image1.size == image2.size and list(image1.getdata()) == list(image2.getdata()):
        print(f"Images {file} are identical.")
        return True
    else:
        print(f"Images {file} are not identical.")
        return False