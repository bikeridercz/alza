from selenium import webdriver
import os, time, datetime;

driver = webdriver.Chrome()

while True:
	driver.get("https://www.alza.cz/gaming/asus-rog-strix-geforce-rtx-3080-gaming-o10g-d6150802.htm")
	#driver.get("https://www.alza.cz/gigabyte-geforce-gtx-1650-d6-oc-4g-d5844043.htm")

	polozka=driver.find_elements_by_xpath('.//span[contains(@class, "stcTitle")]')[0].get_attribute("title")
	sklad=driver.find_elements_by_xpath('.//span[contains(@class, "stcStock")]')[0].get_attribute("title")

	print(datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"), " - ", polozka, ' ---> ', sklad)
	if "Skladem" in sklad:
		os.system("say Už to přišlo")


	time.sleep(60)

driver.stop_client()
driver.close()
