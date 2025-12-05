import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import mysql.connector
import requests
from bs4 import BeautifulSoup

from omkar import response

#Fetching web data:
url="https://www.worldometers.info/coronavirus/"
response=requests.get(url)
soup=BeautifulSoup()


