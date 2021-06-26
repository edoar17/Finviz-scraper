# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 01:49:39 2021

@author: edoar
"""

# Download finbox table
# Market Cap > 1 billion, P/E ratio > 0

from selenium import webdriver
from selenium.webdriver.support.select import Select
import math
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import urllib3

# Set up chrome driver
url = 'https://finviz.com/screener.ashx?&ft=4'
driver = webdriver.Chrome(r'C:\Users\edoar\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)

# Filtering parameters, dictionary of form {element id: option}
params = {
    'fs_exch':'NASDAQ', 
    'fs_fa_pe': 'Under 15'}

def filterStocks(params):
    
    # Filter stocks in finviz
    def selectFilters(params):
        """ Dictionary of {elementID: option} """
        for para in params:
            elementID = para
            option = params.get(elementID)
            dropdownmenu = driver.find_element_by_id(elementID)
            sel = Select(dropdownmenu)
            sel.select_by_visible_text(option)        
    selectFilters(params) 
     
    # Get stocks list
    symbols = driver.find_elements_by_class_name('screener-link-primary')
    ticker_list = []
    for sym in symbols:
        ticker_list.append(sym.text)
        
    # driver.quit()
    weburl = driver.current_url
    return ticker_list
  
# Downloads first page of stocks table
a = filterStocks(params)



url = 'https://finviz.com/screener.ashx?&ft=4'
driver = webdriver.Chrome(r'C:\Users\edoar\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)

N_of_ticks = 50
N_of_pages = math.ceil(N_of_ticks/20)
pages = driver.find_elements_by_class_name('body-table screener_pagination')

weburl = driver.current_url
driver.quit()

http = urllib3.PoolManager()
req = http.request("GET", "https://finviz.com/screener.ashx?&ft=4")
soup = BeautifulSoup(req.data, 'html.parser')
table = soup.find_all('a', class_='screener-link-primary')

access_token = req.data.decode('UTF-8')
req.data


for a in soup.find_all('a', class_='screener-link-primary'):
    print("Found the URL:", a['href']) 


yyy = []
for i in range(1,N_of_pages):
    xxx = weburl + '&r=' + str(1+i*20) 
    driver.get(xxx)
    yyy = driver.find_elements_by_class_name('screener-link-primary')
    print(xxx)
    
    
    
    














