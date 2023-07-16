from PIL import Image
import random

nums_bound = [11, 50, 400, 1600, 6400, 40000]
scales = [3, 2, 1, 0.5, 0.25, 0.1]

def generate_point_list(num, max_x, max_y):
    coordinates = []

    for _ in range(num):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        coordinates.append((x, y))
        
    # Sort the coordinates by the y-axis
    coordinates.sort(key=lambda coord: coord[1])
    
    return coordinates

def resize_image(img, scale):

    if scale == 1:
        return img

    # Calculate the new size based on the scaling factor
    width = int(img.width * scale)
    height = int(img.height * scale)

    # Resize the image using Bicubic interpolation
    resized_img = img.resize((width, height), Image.BICUBIC)

    # Return the resized image
    return resized_img

def place_image_random(path, num_placements):
    sc = 1
    for (num, scale) in zip(nums_bound, scales):
        if num_placements < num:
            sc = scale
            break
    img = Image.open(path)
    img = resize_image(img, sc)
    imf = img.transpose(Image.FLIP_LEFT_RIGHT)
    width, height = 5000, 5000
    canvas_color = (255, 255, 255)  # Replace with the desired canvas color in RGB format

    max_x = width - img.width
    max_y = height - img.height

    # Create a new blank canvas with the desired color
    canvas = Image.new('RGBA', (width, height), canvas_color)

    coordinates = generate_point_list(num_placements, max_x, max_y)

    for coord in coordinates:
        x, y = coord

        if random.random() < 0.5:
            canvas.paste(img, (x, y), img)
        else:
            canvas.paste(imf, (x, y), imf)

    # Save the modified canvas
    canvas.save('output.png')
    canvas.show()

# Usage example
image_path = './mumuu.png'  # Replace with your image file path
# like + share + comment
# 19h00 16/7: 32 + 12 + 4
# 20h00 16/7: 59 + 15 + 4
# 21h30 16/7: 65 + 16 + 6
num_placements = 99  # Number of times to place the image

place_image_random(image_path, num_placements)
