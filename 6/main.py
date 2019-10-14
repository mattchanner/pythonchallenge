import urllib2
from PIL import Image

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/channel.jpg")
contents = response.read()

original = Image.open(contents)
print original