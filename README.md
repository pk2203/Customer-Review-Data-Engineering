# Data Engineering Analytics 
## Web Scraping
 This repo contains python code done to extract customer reviews from various website URL's including google play and google maps. Done with Python 3.11 on Visual Studio Code platform. Some of the main libraries used:
> + `from selenium.webdriver.common.by import By`
> + `from selenium import webdriver`
> + `from bs4 import BeautifulSoup`
>   
 While **[Selenium](https://selenium-python.readthedocs.io/index.html)** is a library mostly used for conduction automated unit testings in Python ide framework, this was used here to automate the naviagation of websites to make it easier to extract data. **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** is an efficient library to work with html contents as it does an excellent job with parsing and makes it easier to find the xpaths required. 
Further libraries involved for generating quick csv files involved `pandas` and `numpy`.

## REST APIs
  Many applications allows API belonging to **Representation State Transfer(REST)** category. This allows to perform RESTful operartions like reading, modifying, adding or deleting data from the source application. The APIs worked in the repos to extract customer services data also supports **[Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)**
  Some of the usable API commands are:
  | Command | Purpose                      |
  |---------|------------------------------|
  | POST    | Create an Object             |
  | GET     | Fetch one or more objects    |
  | PUT     | Update an object             |
  | DELETE  | Remove an object             |

  This was done with Python 3.11 with Visual Studio Code. The used libraries involve:
> + `import json`
> + `import requests`
> + `import pandas as pd`
>
  The APIs are plain JSON content over HTTP which is why **[requests](https://realpython.com/python-requests/)** library module is used to _GET_ the data content from the API on which **[json](https://www.programiz.com/python-programming/json)** is used to parse the decoded content. This is stored to immediately generate a csv or xlsx file using `pandas` library. 
  
  
