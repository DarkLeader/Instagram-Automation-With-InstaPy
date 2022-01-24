import requests
from bs4 import BeautifulSoup
import csv
#CSV = 'database.csv'

source = requests.get('https://www.entrepreneur.com/franchise500')
source.raise_for_status()

soup = BeautifulSoup(source.text,'html.parser')

#container = soup.find('div', id="containerDom").find('div', id='childContainerDom').find('div', class_='bg-white shadow overflow-hidden sm:rounded-md mb-4').find_all('li', class_='border-b')

def get_names():

    divs = soup.find('div', id="containerDom").find('div', id='childContainerDom').find_all('div')
    data_list = []
    for div in divs:
        needed_div = div.find('div', class_='bg-white shadow overflow-hidden sm:rounded-md mb-4')
        if needed_div:
            franchises = needed_div.find_all('li', class_='border-b')
            for franchise in franchises:
                name = franchise.find('p', class_="text-base font-medium text-gray-700 truncate w-1/2")
                category = franchise.find('p', class_="text-sm font-medium text-gray-700")
                description = franchise.find('p', class_="mt-1 flex items-center text-sm text-gray-700")
                initial = franchise.find('p', class_="text-sm text-gray-700")


                try:

                    data = {
                        "name": name.text.replace("Request Info", "").strip(),
                        "category": category.text.strip(),
                        "description": description.text.strip(),
                        "initial": initial.text.strip(),
                    }
                    data_list.append(data)
                except:
                    pass


    return data_list

print(len(get_names()) == 50)
data = get_names()
with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'category', 'description', 'initial'])
    writer.writeheader()
    writer.writerows(data)
