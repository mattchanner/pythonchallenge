import pickle
import urllib2

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(response)
fp = open("output.txt", "w")
for line in data:
    for tup in line:
        char, num = tup
        fp.write(char * num)        
fp.close()

# channel
