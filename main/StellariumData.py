import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


URL = "https://stellarium-web.org/skysource/Pleiades?fov=0.00027778&date=2021-09-11T05:58:58Z&lat=40.97&lng=-76.91&elev=0"
driver = webdriver.Firefox()
driver.get(URL)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

soup.findAll("div", {"class": "radecVal"})
print(soup.text)
