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
import urllib.request

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


# Retrive n of ticks from a search query
def retrieveTicks(webUrl, N_of_ticks):
    N_of_pages = math.ceil(N_of_ticks/20)
    #Main page
    ticks = retrieveTicksFromPage(webUrl)
    #Subsequent pages
    for i in range(1,N_of_pages):
        xxx = url + '&r=' + str(1+i*20)
        ticks.extend(retrieveTicksFromPage(xxx))
        print(xxx)
    return ticks[:N_of_ticks]
    
# yyy = retrieveTicks(url, 20) #Test

# Downloads ticks table from url
def retrieveTicksFromPage(webUrl):
    # Get html from main filter page, ft=4 ensures all filters are present
    hdr = {
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) "
           "Chrome/23.0.1271.64 Safari/537.11"
    }
    req = urllib.request.Request(webUrl, headers=hdr)
    with urllib.request.urlopen(req) as response:
                html = response.read().decode("utf-8")
    
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('a', class_='screener-link-primary')
    ticks = []
    for t in table:
        ticks.append(t.text)
    return ticks

    














