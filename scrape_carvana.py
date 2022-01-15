from bs4 import BeautifulSoup
import requests

class URLParser():
	def __init__(self, url):
		self.url = url
		self.soup = BeautifulSoup(requests.get(url).text, "html.parser")

class CarvanaParser(URLParser):
	def __init__(self):
		super().__init__("https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e")

	def get_cars(self):
		return [div.text for div in self.soup.find_all('div', attrs = {"class": "year-make-experiment"})]
		# --- can do python way, but library provides a lot of it ---
		# return [div.text for div in self.soup.find_all('div') if "class" in div.attrs and "year-make-experiment" in div["class"]]

	def get_cars_info(self):
		car_info_dict = {}
		for div in self.soup.find_all('div', attrs = {"class": "result-tile"}):
			name = div.find("div", attrs = {"class": "year-make-experiment"}).text
			sub_page_parser = CarvanaResultParser("https://www.carvana.com" + div.a["href"])
			car_info_dict[name] = sub_page_parser.get_result_car_info()
			print("Car: " + name)
		return car_info_dict

class CarvanaResultParser(URLParser):
	def __init__(self, url):
		super().__init__(url)

	def get_result_car_info(self):
		basic_info = self.soup.find("div", attrs = {"data-qa": "price-wrapper"})
		return [div.text for div in basic_info.find_all("div")] if basic_info != None else ["None"]


def main():
	parser = CarvanaParser()
	print("\n".join([str(index) + ": " + car for index, car in enumerate(parser.get_cars())]))
	for key, value in parser.get_cars_info().items():
		print(key)
		for info_piece in value:
			print("   " + info_piece)
		print()
	# print(parse.soup.findall("div"))

if __name__ == "__main__":
	main()


"""
https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e

https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e
"""