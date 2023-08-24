import pandas as pd 
import numpy as np 
from datetime import datetime
import time
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

WebPageURL = "https://play.google.com/store/apps/details?id=com.barakat&hl=en&gl=US"

class BKReviews:

    def __init__(self, debug=False):
        self.Date = []
        self.Name = []
        self.Review = []
        self.Comments = []
        self.Rating = []
        self.debug = debug
        self.driver = self.__get_driver()
        self.logger = self.__get_logger()
    
    def __scroll(self):
        scrollable_div = self.driver.find_element(By.XPATH,'//div[@jsname="bN97Pc"]')
    
        for i in range(0,10):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        
    
    def __expand_reviews(self):
        # use XPath to load complete reviews
        link = self.driver.find_element(By.XPATH,'//button[@aria-label="See more information on Ratings and reviews"]')
        link.click()
        time.sleep(2)
    
    def __sort_reviews(self):
        link = self.driver.find_element(By.XPATH,'//div[@id="sortBy_1"]')
        link.click()
        time.sleep(2)

        newest = self.driver.find_element(By.XPATH,'//span[@aria-label="Rating"]')
        newest.click()
        time.sleep(2)
    
        
    def __get_driver(self):
        print("Attaching WebDriver")
   
        input_driver = webdriver.Chrome()
        input_driver.get(WebPageURL)

        print("WebDriver Attached")

        return input_driver
    
    def extract_data(self):
        self.__expand_reviews()
        self.__sort_reviews()
        self.__scroll()     

        content = self.driver.page_source
        soup = BeautifulSoup(content,features="html.parser")   
    
        for name in self.driver.find_elements(By.XPATH,"//div[@class='RHo1pe']//div[@class='X5PpBb']"):
            print(name.text)
            self.Name.append(name.text)
        print(len(self.Name))
        for date in soup.findAll('span',attrs={'class':'bp9Aid'}):
            print(date.text)
            self.Date.append(date.text)
        print(len(self.Date))
        for rate in soup.findAll('div',attrs={'role':'img','class':'iXRFPc'}):
            self.Rating.append(rate['aria-label'])
        print(len(self.Rating))
        for review in soup.findAll('div',attrs={'class':'h3YV2d'}):
            self.Review.append(review.text)
        print(len(self.Review))


        print("Finished extraction")
        
    def get_data(self):
        df = pd.DataFrame({'Name':self.Name,'Date':self.Date[3:],'Review':self.Review[3:],'Rate':self.Rating[3:]})
        df.to_csv('bkreview.csv',index=False,encoding='utf-8')

if __name__ == "__main__":
    new_rev = BKReviews()
    new_rev.extract_data()
    new_rev.get_data()

    




            
        





