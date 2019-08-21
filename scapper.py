from bs4 import BeautifulSoup



def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# add_divs = soup.find_all('div',attrs={'class':'crux-body-copy'}) 

# for div in add_divs:
#      print(div.a.string)

product_names = [div.a.string for div in soup.find_all('div', class_ ='crux-body-copy')]
product_links = [div.a['href'] for div in soup.find_all('div', class_ ='crux-body-copy')]

products = {div.a.string:div.a['href'] for div in soup.find_all('div',class_='crux-body-copy')}
# for product in products:
#     print(product)

for key, value in products.items():
    print(key,' -->',value)