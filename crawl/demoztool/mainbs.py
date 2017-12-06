#!/usr/bin/env python
# coding: utf-8

import requests
import threading
import time
import sys

from bs4 import BeautifulSoup
from pprint import pprint
from json import dumps,loads
from Queue import Queue

from db.url_dao import UrlDao
from dmzbs import Dmzbs
from db.url_mysql_dao import UrlMysqlDao

CONF = loads(open("./config.json").read())

print_lock = threading.Lock()
# dmzhome = requests.get("http://dmoztools.net/World/")

DOMAIN_NAME = CONF['domain_name']
FORCE_CHECK = CONF['force_check']

urldao = UrlDao();
# url_mysql_dao = UrlMysqlDao();
link_queue = Queue()

def combine_url(url):
    return DOMAIN_NAME+url

def url_to_keyword(url):
    return "~".join( list( filter(None, url.split('/') ) )[2:] )

def check_link_data(url):
    mydata = threading.local()
    mydata.path_url = url
    mydata.keyword = url_to_keyword(mydata.path_url)
    mydata.url = combine_url(mydata.path_url)
    # mydata.source = requests.get(mydata.url)
    # mydata.dmzbs = Dmzbs(mydata.source.content)

    print mydata.path_url 
    print mydata.keyword

    # urldao.insert(mydata.url,mydata.dmzbs.node_count,mydata.dmzbs.last_update)
    # if mydata.dmzbs.site_list : 
    #     url_mysql_dao.insert_many_url_same_keyword(mydata.keyword,mydata.dmzbs.site_list)
    
    # for mydata.sub_categories in mydata.dmzbs.sub_categories:
    #     if ( not FORCE_CHECK and urldao.is_url_exist( combine_url(mydata.sub_categories['url']),mydata.sub_categories['node_count']) is not None ):
    #         continue

    #     link_queue.put( mydata.sub_categories['url'] )


def process_queue():
    while True:
        link = link_queue.get()
        check_link_data(link)
        link_queue.task_done()

for i in range(4):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

for lang in CONF['languages']:
    link_queue.put( lang['link'] )
    # link_queue.put( "/World/Bahasa_Indonesia/Olahraga/")
    break;

start = time.time()
link_queue.join()
print("Execution time = {0:.5f}".format(time.time() - start))