from PIL import Image

img = Image.open("oxygen.png")
row = [img.getpixel((x, int(img.height / 2))) for x in range(img.width)]

# colours are in blocks 7 pixels wide, so use this as the stride
chars = [chr(r) for r, g, b, a in row[::7] if r == g == b]

print(''.join(chars))

# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
hint = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(x) for x in hint))
# integrity
