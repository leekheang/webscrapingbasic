from bs4 import BeautifulSoup



def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

add_divs = soup.find_all('div',attrs={'class':'crux-body-copy'}) 

# for div in add_divs:
#      print(div.a.string)

products = [div.a.string for div in add_divs]
for product in products:
    print(product)