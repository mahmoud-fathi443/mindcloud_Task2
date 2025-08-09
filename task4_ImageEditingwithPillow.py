from PIL import Image

image = Image.open('image.jpg')

pixel_map = image.load()

width, height = image.size

black = (0, 0, 0)
for i in range(width//4):
    for j in range(height):
        pixel_map[i, j] = black


image.show()
image.save('new_image.png')