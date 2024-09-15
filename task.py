import requests
from bs4 import BeautifulSoup as bs

company_names_lst = []
company_ticker_lst = []
market_cap_lst = []
categories_for_company_lst = []

response = requests.get("https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/")

soup = bs(response.content, 'html.parser')

market_cap_lst = soup.select(".name-td+ .td-right")

td_lst = market_cap_lst.select('td')









#print(market_cap_lst)