import requests
import csv
import re 
from urlextract import URLExtract
import pandas as pd

data = """%CroppedText.Trimmed.Trimmed%"""
print(data)
extractor = URLExtract()
url = extractor.find_urls(data)
new_url = url[0]
print(new_url)

r1 = requests.get(new_url)
print("Got r1")

if r1.status_code == 404:
	print("Not occured")
else:
	decoded_content = r1.content.decode('utf-8')
	print(decoded_content)
