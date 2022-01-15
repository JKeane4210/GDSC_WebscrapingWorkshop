# from selenium import webdriver
# from webdriver_manager.driver import ChromeDriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException as SeleniumNoSuchElementException
# from selenium.webdriver.chrome.options import Options
# import time

# # start web browser
# options = Options()
# options.add_argument("--headless")
# browser = webdriver.Chrome(ChromeDriverManager().install(), options = options)

# # get source code
# browser.get("https://www.carmax.com")
# browser.minimize_window()
# html = browser.page_source
# print(html)

import requests

url = "https://www.carvana.com/cars/in-milwaukee-wi?utm_source=bing&utm_medium=sem_b&utm_term=1&utm_campaign=382591011&utm_content=1207264226548752&utm_target=kwd-75454349431947:loc-71239&utm_creative=&utm_device=c&utm_adposition=&utm_rw=1&msclkid=887aa899dff915ff2bccc97af1b79c2e"
r = requests.get(url)
print(r.text)