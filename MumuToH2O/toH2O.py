from PIL import Image, ImageDraw
import numpy as np

# Load the image
image_path = "./orig.png" # replace with your image path
img = Image.open(image_path).convert('L')  # Convert to grayscale

# Scale the image by a factor of 2
img = img.resize((img.size[0]*2, img.size[1]*2), Image.NEAREST)

# Get the pixel data
data = np.array(img)

# Create a blank image to draw the text on
scale_factor = 9
blank_img = Image.new('L', (data.shape[1]*scale_factor, data.shape[0]*scale_factor), color=255)
d = ImageDraw.Draw(blank_img)

# Iterate over each pixel pair
for y in range(0, data.shape[0]):
    for x in range(0, data.shape[1], 2):
        # If both pixels in the pair have a value less than 128, add "H2O" text
        if data[y, x] < 128 and data[y, x+1] < 255:
            d.text((x*scale_factor, y*scale_factor), "H2O", fill=0)
            d.point((x*scale_factor + 5, y*scale_factor + 3), fill=255)
            d.point((x*scale_factor + 5, y*scale_factor + 8), fill=255)

# Show the result
blank_img.show()
blank_img.save("output.png")
