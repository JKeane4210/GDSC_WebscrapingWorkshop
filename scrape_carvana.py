from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

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
		all_car_info_dict = {}
		for div in self.soup.find_all('div', attrs = {"class": "result-tile"}):
			name = div.find("div", attrs = {"class": "year-make-experiment"}).text
			sub_page_parser = CarvanaResultParser("https://www.carvana.com" + div.a["href"])
			single_car_info = sub_page_parser.get_result_car_info()
			if re.search(r"\$[,\d]+", single_car_info[0]) and re.search(r"[,\d]+ miles", single_car_info[1]):
				# only want the cars that give price and total miles
				single_car_info = [int(re.sub(r"[^\d]", "", s)) for s in single_car_info]
				single_car_info_dict = {}
				single_car_info_dict["price"] = single_car_info[0]
				single_car_info_dict["miles"] = single_car_info[1]
				single_car_info_dict["link"] = div.a["href"]
				all_car_info_dict[name] = single_car_info_dict
				print("Car: " + name)
		return all_car_info_dict

class CarvanaResultParser(URLParser):
	def __init__(self, url):
		super().__init__(url)

	def get_result_car_info(self):
		basic_info = self.soup.find("div", attrs = {"data-qa": "price-wrapper"})
		return [div.text for div in basic_info.find_all("div")] if basic_info != None else ["None"]

def main():
	parser = CarvanaParser()
	# demonstrating getting cars names
	print("\n".join([str(index) + ": " + car for index, car in enumerate(parser.get_cars())]))
	print()
	# demonstrating getting cars and evaluatable information
	car_search_results_dict = parser.get_cars_info()
	for car, car_props in car_search_results_dict.items():
		print(car)
		for car_prop, car_prop_value in car_props.items():
			print("   " + car_prop + ": " + str(car_prop_value))
		print()
	# creating a DataFrame to hold the information and output it to a CSV
	df = pd.DataFrame(car_search_results_dict).T
	print(df.head())
	df.to_csv("car_search_results_dict.csv")

if __name__ == "__main__":
	main()


"""
https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e

https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e
"""