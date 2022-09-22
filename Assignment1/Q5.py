import re
from mechanize import Browser


def get_html(url):
    br = Browser()
    br.open(url)
    html = br.response().readlines()
    clean = re.compile('<.*?>')
    print(re.sub(clean, '', str(html)))


url = input()
get_html(url)
