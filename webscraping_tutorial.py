from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
url = 'http://webcode.me'
resp = http.request('GET', url)
soup = BeautifulSoup(resp.data.decode('utf-8'), "html.parser")

print(soup.head.title.text)