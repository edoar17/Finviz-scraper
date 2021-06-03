# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 01:49:39 2021

@author: edoar
"""

# Download finbox table
# Market Cap > 1 billion, P/E ratio > 0

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import pandas as pd

# Filtering parameters, {element id: option}
params = {
    'fs_exch':'NASDAQ', 
    'fs_fa_pe': 'Under 15'}

def filterStocks(params):   
    # Set up chrome driver
    url = 'https://finviz.com/screener.ashx?&ft=4'
    driver = webdriver.Chrome(r'C:\Users\edoar\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    
    # Filter stocks in finviz
    def selectFilters(dictionary):
        """ Dictionary of {elementID: option} """
        for di in dictionary:
            elementID = di
            option = dictionary.get(elementID)
            dropdownmenu = driver.find_element_by_id(elementID)
            sel = Select(dropdownmenu)
            sel.select_by_visible_text(option)
            
    selectFilters(params)        
    symbols = driver.find_elements_by_class_name('screener-link-primary')
    ticker_list = []
    for sym in symbols:
        ticker_list.append(sym.text)
    return ticker_list
    
a = filterStocks(params)
    
url = 'https://finviz.com/screener.ashx?&ft=4'
driver = webdriver.Chrome(r'C:\Users\edoar\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)


filt_names = driver.find_elements_by_class_name('screener-combo-title')
filters = []
for txt in filt_names:
    filters.append(txt.text)
    
eles_id_web = driver.find_element_by_xpath("//td[@class='filters-border']").find_elements_by_xpath("//*[contains(@id, 'fs_')]")
elementIds = []
for ide in eles_id_web:
    elementIds.append(ide.get_attribute('id'))

filters_df = pd.DataFrame({'filter_name': filters,
                           'ID': elementIds})   

    
    
    
    
    
    






