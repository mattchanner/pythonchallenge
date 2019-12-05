from urllib.request import urlopen
from PIL import Image

response = urlopen("http://www.pythonchallenge.com/pc/def/channel.jpg")
contents = response.read()

original = Image.open(contents)
print(original)