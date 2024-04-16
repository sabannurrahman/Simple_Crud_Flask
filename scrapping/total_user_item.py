import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5000/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
# find untuk mencari data paling atas saja sedangkan find all untuk semua data
find_data = soup.find_all(id='count_data')
for x in find_data:
    print(x.text)

# text = find_data.text mengekstrak text saja
# print(find_data.prettify()) menampilkan html dengan rapi


