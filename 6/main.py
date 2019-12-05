import zipfile
import re
from urllib.request import urlopen


def get_next(next_number, zip):
    name = str(next_number) + '.txt'
    entry = zip.open(name)
    contents = entry.read().decode('utf-8')    
    comment = zip.getinfo(name).comment.decode('utf-8')
    matches = re.findall("Next nothing is (\d+)", contents)
    return (contents, comment, matches[0] if len(matches) else '')


response = urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
contents = response.read()

with open('channel.zip', 'wb') as fp:
    fp.write(contents)

zip_file = zipfile.ZipFile('channel.zip')
next_number = 90052

comments = ""

while True:
    contents, comment, next_number = get_next(next_number, zip_file)
    comments += comment
    if not next_number:
        break

print(comments)
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
# **************************************************************
