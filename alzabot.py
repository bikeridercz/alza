from selenium import webdriver
import os
import config

driver = webdriver.Chrome()

for i in config.itemList:
	driver.get(i)

	itemName = driver.find_elements_by_xpath('.//div[@class="stcInfoContent"]/span[@class="stcTitle"]')[0].get_attribute("title")
	avlText = driver.find_elements_by_xpath('.//div[@class="stcInfoContent"]/span[contains(@class, "stcStock")]')[0].get_attribute("title") 
	print(itemName, ': ', avlText)

	driver.stop_client()
	
	if avlText != "Těšíme se":
		os.system("say karta je skladem")

driver.close()
