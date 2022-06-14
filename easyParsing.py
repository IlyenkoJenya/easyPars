import requests
from bs4 import BeautifulSoup as bs
import time
URL_TEMPLATE = "https://www.sushi-profi.ru/menu/teplye-rolly/"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all(['li','p'], class_=['product lucky-product-False product-data', 
'product with-accent lucky-product-False product-data',])
vacancies_price=soup.find_all( 'p', class_='product-price product-price--teplye-rolly')
names=[]
prices=[]
print ('Теплые роллы - цена')
def parsing():
	for name in vacancies_names:
		names.append(name['data-title'])
	for price in vacancies_price:
		prices.append(price.span.string)
	
	results_dict=dict(zip(names,prices))

	for key in results_dict:
		print (key,'-', results_dict[key],'rub')

parsing()
time.sleep(5)