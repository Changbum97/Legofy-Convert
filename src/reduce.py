from PIL import Image
import os

def reduce_colors(img, num_colors):
    # Convert the image to RGB mode (if it's not already)
    img = img.convert('RGB')

    # Reduce the number of unique colors
    img = img.quantize(colors=num_colors)

    # Convert the image back to its original mode
    img = img.convert('RGB')

    return img

if __name__ == '__main__':

    image_path = os.path.realpath('../assets/images/양파쿵야.jpeg')

    # Load the image
    img = Image.open(image_path)

    # Reduce the number of colors to 16
    img = reduce_colors(img, 16)

    # Save the output image
    img.save('../assets/images/양파쿵야-2.png')
