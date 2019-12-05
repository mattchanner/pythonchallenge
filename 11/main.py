from PIL import Image


image = Image.open("cave.jpg")
width, height = image.size

odd = Image.new('RGB', (width // 2, height // 2))
even = Image.new('RGB', (width // 2, height // 2))

for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y))
        if x % 2 == 0:
            odd.putpixel((x // 2, y // 2), pixel)
        else:
            even.putpixel((x // 2, y // 2), pixel)

odd.save("odd.jpg")
even.save("even.jpg")
