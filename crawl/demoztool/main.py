from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint

from db.UrlDao import UrlDao

urlDao = UrlDao()
urlDao.createTable()


driver = webdriver.Chrome('/var/opt/selenium-driver/chromedriver')
driver.get("http://dmoztools.net/")

pageSource = driver.page_source

elLang = driver.find_element_by_css_selector("#home-cat-world .top-cat a")
link = elLang.get_attribute('href')

elLang.click()

# driver change due to redirect href
# search href contains indonesia with ignore case
elIdLink = driver.find_element_by_css_selector("#cat-list-content-main .cat-item a[href*='indonesia' i]")
elIdLink.click()

# driver change due to redirect href
elCategories = driver.find_elements_by_css_selector("#cat-list-content-2 .cat-item a")

for elCategory in elCategories:
	print elCategory.get_attribute('href')

pageSource = driver.page_source
driver.close()

# soup = BeautifulSoup(pageSource, 'html.parser')
# links = soup.select("#cat-list-content-2 .cat-item a")

# for link in links:
# 	print link.get('href') #uncompleted url

# print(soup.prettify())