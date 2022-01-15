from bs4 import BeautifulSoup
import requests

class URLParser():
	def __init__(self, url):
		self.url = url
		self.soup = BeautifulSoup(requests.get(url).text, "html.parser")

class CarvanaParser(URLParser):
	def __init__(self):
		self.url = "https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e"
		super().__init__(self.url)

	def get_cars(self):
		return [div.text for div in self.soup.find_all('div') if "class" in div.attrs and "year-make-experiment" in div["class"]]


def main():
	parser = CarvanaParser()
	print("\n".join([str(index) + ": " + car for index, car in enumerate(parser.get_cars())]))
	# print(parse.soup.findall("div"))

if __name__ == "__main__":
	main()


"""
https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e

https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e
"""