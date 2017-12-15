#!/usr/bin/env python
# coding: utf-8

# webdev1dn2016!!


import requests
import threading
import time
import sys
import logging
import urllib 

from bs4 import BeautifulSoup
from pprint import pprint
from Queue import Queue

from db.url_dao import UrlDao
from db.unfinished_url_dao import UnfinishedUrlDao
from dmzbs import Dmzbs
from db.url_mysql_dao import UrlMysqlDao
from dmz_config import DmzConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_handler = logging.FileHandler('dmztool_crawl_logging.log')
logger_handler.setLevel(logging.DEBUG)
logger_formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)

urldao = UrlDao();
unfinished_url_dao = UnfinishedUrlDao();
# url_mysql_dao = UrlMysqlDao();
link_queue = Queue()
DMZCONFIG = DmzConfig()

request_num = 0
sleep_time = 0

lock = threading.Lock()

def initiate():
    global sleep_time
    global request_num

    logger.info("initiate")

    request_num = 0
    sleep_time = DMZCONFIG.SLEEP_FINISHED
    unfinished_urls = unfinished_url_dao.get_all()
    logger.debug("INITIATE unfinished urls {} ".format(unfinished_urls))

    if not unfinished_urls:
        logger.info("initate by config")
        for lang in DMZCONFIG.LANGUAGES:
            link_queue.put( lang['link'] )
    else:
        logger.info("initate unfinished urls")
        for un_url in unfinished_urls:
            link_queue.put( un_url[1] ) 

def combine_url(url):
    return DMZCONFIG.DOMAIN_NAME+url

def url_to_keyword(url):
    return "~".join( list( filter(None, urllib.unquote(url.encode('utf-8', 'ignore')).split('/') ) ) ) 

def check_link_data(url):
    global sleep_time
    global request_num
    global lock

    try:
        logger.info("processing "+url)

        mydata = threading.local()
        mydata.url = url
        mydata.keyword = url_to_keyword(mydata.url)
        mydata.complete_url = combine_url(mydata.url)

        mydata.request = requests.get(mydata.complete_url)
        logger.info("#REQUEST {} {} ".format(mydata.complete_url,mydata.request.status_code))        

        if mydata.request.status_code is not 200 :
            
            # remove url from queue when status code not 200 
            while not link_queue.empty():
                link_queue.get_nowait()

            logger.warning('{} {}'.format(mydata.url,mydata.request.status_code))
            return

        mydata.dmzbs = Dmzbs(mydata.request.content)
        mydata.sub_categories = mydata.dmzbs.sub_categories


        return 
        for mydata.sub_category in mydata.sub_categories:
            mydata.sub_category['url_data'] = urldao.get_url( mydata.sub_category['url'],mydata.sub_category['node_count'])

            # save as unfinished url when url and node_count not match in table "url" 
            if ( DMZCONFIG.FORCE_CHECK or mydata.sub_category['url_data'] is None ):
                lock.acquire()
                unfinished_url_dao.insert(mydata.sub_category['url'],mydata.sub_category['node_count'])
                lock.release()

        if mydata.dmzbs.site_list :
            #save all url list to db 
            url_mysql_dao.insert_many_url_same_keyword(mydata.keyword,mydata.dmzbs.site_list)
        
        # save url to queue when max request is greater or equal ro current passed request number plus length of sub directory 
        if DMZCONFIG.MAX_REQUEST >= ( request_num + len(mydata.sub_categories) ) :
            for mydata.sub_category in mydata.sub_categories:
                # when sub category matched url and node_count doesnt exis in table "url", then put url to queue 
                if ( DMZCONFIG.FORCE_CHECK or mydata.sub_category['url_data'] is None ):
                    link_queue.put( mydata.sub_category['url'])
        else :
            sleep_time = DMZCONFIG.SLEEP_MAX_REQUEST

        #save current url to sqlite table "url". which is later used when checking node_count. this url finished
        lock.acquire()
        urldao.insert(mydata.url,mydata.dmzbs.node_count,mydata.dmzbs.last_update)
        lock.release()
        
        # delete url from unfinished. this url finished
        lock.acquire()
        unfinished_url_dao.delete_by_url(mydata.url)
        lock.release()
        logger.info("done processing {}".format(mydata.url))

        time.sleep(DMZCONFIG.SLEEP_AFTER_REQUEST)

    except IndexError as ie:
        logger.error("{} Error generating node_count or last_update ".format(mydata.url))
    except:
        logger.error("Error : {} {} Error on line {}".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[-1].tb_lineno))

def process_queue():
    while True:
        link = link_queue.get()
        check_link_data(link)
        link_queue.task_done()

for i in range(2):
    t = threading.Thread(target=process_queue)
    mydata = threading.local()
    t.daemon = True
    t.start()

while True:
    initiate()
    link_queue.join()
    time.sleep(sleep_time)

# start = time.time()
# print("Execution time = {0:.5f}".format(time.time() - start))