from urllib.request import urlopen
import re

def get_next(number):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(number)
    response = urlopen(url)
    contents = response.read()
    matches = re.findall("the next nothing is (\d+)", contents)
    return (contents, matches[0] if len(matches) else '')


next_nothing = 12345
next_nothing = 16044 / 2
while True:
    contents, next_nothing = get_next(next_nothing)
    print(contents)
    print(next_nothing)
    if not next_nothing:
        break

# peak.html
