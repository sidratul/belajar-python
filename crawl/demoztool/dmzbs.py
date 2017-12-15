import re

from bs4 import BeautifulSoup

class Dmzbs:
	NODE_COUNT_SELECTOR = "#doc .current-cat .node-count"	
	LAST_UPDATE_SELECTOR = ".last-update .last-update"	
	SUB_CATEGORIES_SELECTOR = "#subcategories-div .cat-item a"	
	SEE_ALSO_SELECTOR = "#related-section .see-also-row a"	
	SITE_LIST_SELECTOR = "#site-list-content .title-and-desc a"	

	def __init__(self,source):
		self.soup = BeautifulSoup(source, 'html.parser')
		self.node_count = int(re.sub('\,', '',(self.soup.select(self.NODE_COUNT_SELECTOR))[0].text))
		self.last_update = (self.soup.select(self.LAST_UPDATE_SELECTOR))[0].text 

		sub_categories = self.soup.select(self.SUB_CATEGORIES_SELECTOR) 
		see_also_categories = self.soup.select(self.SEE_ALSO_SELECTOR) 

		self.sub_categories = []

		for category in sub_categories + see_also_categories:
			self.sub_categories.append({
				'url' : category.get('href'),
				'node_count' : int(re.sub('\,', '', category.select('.node-count')[0].text))
			})

		site_list = self.soup.select(self.SITE_LIST_SELECTOR)
		self.site_list = []
		for site in site_list:
			self.site_list.append( site.get('href') )

		return