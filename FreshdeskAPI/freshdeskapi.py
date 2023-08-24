import json
import requests
import pandas as pd

class freshdesk:
    def __init__(self,url,api_key,page_limit,debug=False):
        self.debug = debug 
        self.page_limit = page_limit
        self.url = url
        self.api_key = api_key
        self.response = self.__get_response()
        self.data = pd.DataFrame()
    
    def __get_response(self,start_response=True):
        FRESHDESK_ENDPOINT = self.url
        FRESHDESK_KEY = self.api_key
        page_num = 1
        print("Starting")

        while start_response:
                response = requests.get(FRESHDESK_ENDPOINT+f"/helpdesk/tickets/filter/all_tickets?format=json&page={page_num}"
                                                         ,auth=(FRESHDESK_KEY, "X"))
                try:
                    if response.status_code == 200:
                        print(f"Response {page_num}")
                        yield response 
                except:
                    response.raise_for_status()
                    start_response = False

                page_num = page_num+1
                if page_num > self.page_limit:
                    start_response = False
    
    def get_users(self):
        FRESHDESK_ENDPOINT = self.url
        FRESHDESK_KEY = self.api_key

        users = requests.get(FRESHDESK_ENDPOINT+"/contacts.json",auth=(FRESHDESK_KEY, "X"))
        

    def extract_data(self): 
        appended_data = []
        for r in self.response:
            temp = pd.DataFrame(r.json())
            appended_data.append(temp)

        self.data = pd.concat(appended_data)

    def print_data(self):
        print(self.data.head())
        print(self.data.info())
    
    def get_csv(self):
        self.data.to_csv('bkfreshdesk.csv',index=False,encoding='utf-8')
    
if __name__ == "__main__":
    # url = "{To be mentioned}" 
    # api_key = "{To be mentioned}" 
    fd = freshdesk(url,api_key,page_limit=45)
    fd.extract_data()
    fd.print_data()
    fd.get_csv()

    



    

