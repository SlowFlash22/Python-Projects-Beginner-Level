from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from web_scraping import all_links, all_prices, all_address
from dotenv import load_dotenv
import os
load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
FORM_LINK = os.environ.get("FORM_LINK")

for n in range(len(all_links)):

    driver.get(FORM_LINK)
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address.send_keys(all_address[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()