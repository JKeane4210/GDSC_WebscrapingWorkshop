from bs4 import BeautifulSoup
import urllib3

class URLParser():
	def __init__(self, url):
		self.url = url
		self.http = urllib3.PoolManager()
		self.soup = BeautifulSoup(self.http.request('GET', url).data.decode('utf-8'), "html.parser")

def main():
	parser = URLParser("https://www.carmax.com/cars")
	print(parser.soup)
	print(parser.soup.find_all("span", {"class":"refinement-value--name"}))

if __name__ == "__main__":
	main()
