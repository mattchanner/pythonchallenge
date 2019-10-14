import urllib2
import re

def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()

def get_code_behind_comment(url):
    html = get_html(url)
    if not html: return ""

