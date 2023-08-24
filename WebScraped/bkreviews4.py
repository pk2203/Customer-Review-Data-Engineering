import pandas as pd 
import numpy as np 
from datetime import datetime
import time
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

WebPageURL = "https://www.google.com/search?q=barakat+fresh&rlz=1C1GCEU_enAE1061AE1061&oq=barakat+fresh+&aqs=chrome..69i57j0i512l9.3650j0j7&sourceid=chrome&ie=UTF-8"

class BKReviews4:

    def __init__(self):
        self.Date = []
        self.Name = []
        self.Review = []
        self.Comments = []
        self.Rating = []
        self.driver = self.__get_driver()
    
    def __scroll(self):
        scrollable_div = self.driver.find_element(By.XPATH,'//div[@class="review-dialog-list"]')
    
        for i in range(50):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        
    
    def __expand_reviews(self):
        # use XPath to load complete reviews
        link = self.driver.find_element(By.XPATH,'//a[@jsaction="FNFY6c"]')
        link.click()
        time.sleep(2)
        
    def __get_driver(self):
        options = Options()
        options.add_argument("--accept-lang=en-GB")

        print("Attaching WebDriver")
   
        input_driver = webdriver.Chrome(options=options)
        input_driver.get(WebPageURL)

        print("WebDriver Attached")

        return input_driver
    
    def extract_data(self):
        self.__expand_reviews()
        self.__scroll()     

        content = self.driver.page_source
        soup = BeautifulSoup(content,"html.parser")   
    
        for user in soup.findAll('div',attrs={'class':'TSUbDb'}):
            name = user.find('a',attrs={'class':None})
            self.Name.append(name.text)
        print(len(self.Name))

        dates = [date.text for date in soup.findAll('span',attrs={'class':'dehysf lTi8oc'})]
        for i in range(len(dates)):
            if dates[i] != " ":
                self.Date.append(dates[i])
                if (i+1) != len(dates):
                    dates[i+1] = " "

        print(len(self.Date))

        rates = [rate['aria-label'] for rate in soup.findAll('span',attrs={'class':'lTi8oc z3HNkc','role':'img'})]
        for i in range(len(rates)):
            if rates[i] != " ":
                self.Rating.append(rates[i])
                if (i+1) != len(rates): rates[i+1] = " "

        print(len(self.Rating))

        for reviews in soup.findAll('span',attrs={'jscontroller':'MZnM8e'}):
            review = reviews.find('span',attrs={'class':'review-full-text'})
            if review == None:
                review = reviews.find('span',attrs={'class':None})
                if review == None: 
                    self.Review.append(" ")
                    continue
            if len(review.text) != 0:
                self.Review.append(review.text)
            else: 
                continue
        
        print(len(self.Review))

        print("Finished extraction")
        
    def get_data(self):
        df = pd.DataFrame({'Name':self.Name,'Date':self.Date,'Review':self.Review[:len(self.Name)],'Rate':self.Rating})
        df.to_csv('bkreview_google.csv',index=False,encoding='utf-8')

if __name__ == "__main__":
    new_rev = BKReviews4()
    new_rev.extract_data()
    new_rev.get_data()

    