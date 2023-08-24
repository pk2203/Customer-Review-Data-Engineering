import pandas as pd 
import numpy as np 
from datetime import datetime
import time
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

WebPageURL = "https://nicelocal.ae/dubai/shops/barakat_quality_plus_llc/"

class BKReviews3:

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
    
    def __expand_reviews(self):
        links = self.driver.find_element(By.XPATH,'//div[@class="js-show-more-box.pd-lxl.pt0"]')
        links[0].click()
        time.sleep(2)

    def extract_data(self):

        # self.__expand_reviews()

        content = self.driver.page_source
        soup = BeautifulSoup(content,features="html.parser")   

        for user in soup.findAll('strong',attrs={'class':'z-text--16'}):
            name = user.find('span',attrs={'itemprop':'name'})
            self.Name.append(name.text)
        print(len(self.Name))
        for date in soup.findAll('span',attrs={'z-text--dark-gray'}):
            self.Date.append(date.text[6:35])
        print(len(self.Date[3:]))
        for review in soup.findAll('span',attrs={'dir':"auto",'class':"js-comment-content"}):
            self.Review.append(review.text)
        print(len(self.Review))
        
        
        print("Finished extraction")
    
    def get_data(self):
        df = pd.DataFrame({'Name':self.Name,'Date':self.Date[3:],'Review':self.Review})
        df.to_csv('bkreview3.csv',index=False,encoding='utf-8')

if __name__ == "__main__":
    new_rev = BKReviews3()
    new_rev.extract_data()
    new_rev.get_data()
