import urllib.request

from bs4 import BeautifulSoup

imgUrl = 'http://www.qiushibaike.com/imgrank/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(imgUrl, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
text = urllib.request.urlopen(req)
content = text.read().decode('utf-8')
print(content)

soup = BeautifulSoup.get(content, 'html.parser')
items = soup.select("a div.content span")
for item in items:
    print(item['src'])
