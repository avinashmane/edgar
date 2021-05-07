import pandas as pd
import requests

def getIndexStocks(index='S&P'):

    if index=='S&P': 
        tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', header=0)
        return tables[0]

def getUrl(u):
    # Obtain XBRL text from document
    resp = requests.get(u)
    return resp.text
