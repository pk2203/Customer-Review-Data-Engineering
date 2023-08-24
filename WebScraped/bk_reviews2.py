import pandas as pd 
import numpy as np 
from datetime import datetime
import time
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

WebPageURL = "https://emiratesbz.com/dubai/barakat-quality-plus-llc-26997"

class BKReviews2:

    def __init__(self):
        self.Date = []
        self.Name = []
        self.Review = []
        self.Comments = []
        self.Rating = []
        self.driver = self.__get_driver()
   
    def __get_driver(self):
        print("Attaching WebDriver")
   
        input_driver = webdriver.Chrome()
        input_driver.get(WebPageURL)

        print("WebDriver Attached")

        return input_driver

    def extract_data(self):

        content = self.driver.page_source
        soup = BeautifulSoup(content,features="html.parser")   

        for user in soup.findAll('div',attrs={'class':'user-txt-info'}):
            name = user.find('span',attrs={'class':None})
            self.Name.append(name.text)
        for rating in soup.findAll('span',attrs={'class':'stars-row'}):
            rate = len([rates for rates in rating.findAll('i',attrs={'class':'fa-star'})])
            self.Rating.append(rate)
        for date in soup.findAll('div',attrs={'class':'reviewdate'}):
            self.Date.append(date.text)
        for review in soup.findAll('div',attrs={'class':'review-data'}):
            self.Review.append(review.text)
        
        print("Finished extraction")
    
    def get_data(self):
        df = pd.DataFrame({'Name':self.Name,'Date':self.Date,'Review':self.Review,'Rate':self.Rating[1:]})
        df.to_csv('bkreview2.csv',index=False,encoding='utf-8')

if __name__ == "__main__":
    new_rev = BKReviews2()
    new_rev.extract_data()
    new_rev.get_data()





