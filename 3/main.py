from urllib.request import urlopen
import re


def get_comments(url):
    """ fetches the source html file from the URL and returns the text within the html comments. """
    response = urlopen(url)
    html = response.read()
    return "".join(re.findall("<!--([\w \n]*)-->", html))


# fetch the comment from the source file
comment = get_comments("http://www.pythonchallenge.com/pc/def/equality.html")

# find all lower case chars that are surrounded by **exactly** 3 upper case
print("".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", comment)))
# linkedlist