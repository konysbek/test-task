import requests
from bs4 import BeautifulSoup

SHOP_KZ = 'https://shop.kz/bitrix/catalog_export/yandex.php'
headers = {
    'User-Agent': 'My User Agent 1.0',
}

shop = requests.get(SHOP_KZ, 'lxml', headers=headers)
soup = BeautifulSoup(shop.text, 'lxml')

categories = soup.find('categories')
for category in categories.find_all('category'):
    print(category['id'], category.text)

offers = soup.find_all('offer')
for offer in offers:
    print(offer['id'])
    print(offer.findNext(name='name'))
    # сделать поиск по картинкам
#    print('name: ', offer.findNext(name='name').text)
#    print('articul: ', offer['id'])
#    print('price: ', offer.findNext(name='price').text)
#    print('categoryId: ', offer.findNext(name='categoryId'))
#    #print('description: ', offer.findNext(name='description').text)
#    print('pictures: ', offer.find_all_next(name='picture'))
#    print('#####')
#    print('')
#
