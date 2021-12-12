from selenium import webdriver
import os
import sys, importlib
import time
from datetime import datetime
import config

o = webdriver.ChromeOptions();
#o.add_argument("headless");
#o.add_argument('window-size=1200x600');
driver = webdriver.Chrome(options=o)

while True:

	importlib.reload(sys.modules['config'])

	availability = False
	for page in config.pageList:
		try:
			driver.get(page)

			pageName = driver.find_elements_by_xpath('.//div[contains(@class, "categoryPage") and contains(@class, "categoryPageTitle")]/h1')[0].text
			print("\n*********************\n", datetime.now().strftime("%Y.%m.%d-%H:%M:%S"), 'Kontrola: ', pageName)

			itemList = driver.find_elements_by_xpath('.//div[@class="browsingitemcontainer"]/div[contains(@class, "box") and contains(@class, "browsingitem")]')

			for item in itemList:
				itemName = item.find_elements_by_xpath('.//div[@class="top"]/div[@class="fb"]/a')[0].text
				itemAvailabilityText = item.find_elements_by_xpath('.//div[@class="bottom"]/div[contains(@class, "avl")]/span[contains(@class, "avlVal")]')[0].text
				if "Skladem" in itemAvailabilityText:
					availability = True
					itemAvailabilityText = item.find_elements_by_xpath('.//div[@class="bottom"]/div[@class="price"]/div[@class="priceInner"]/span[@class="c2"]')[0].text

				print(itemName.ljust(40), '\t', itemAvailabilityText)
		except:
			print("Unexpected error:", sys.exc_info()[0])

	if availability:
		while True:
			os.system("say Pozor, už to přišlo")
			time.sleep(5)

	time.sleep(60)

driver.stop_client()
driver.close()
