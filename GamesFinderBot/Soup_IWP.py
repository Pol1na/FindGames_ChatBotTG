import requests
from bs4 import BeautifulSoup

def Parser(url, name_of_game):
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'accept': '*/*'
    }
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    cols = []
    results = []
    result_string = ''


    table = soup.find('table').find('tbody')
    rows = table.findAll('tr')
    for row in rows:
        cols.append(row.findAll('td'))

    for col in range(len(cols)):
        try:
            results.append({
            'name_shop': cols[col][0].get_text(strip=True).upper(),
            'price': cols[col][1].get_text(strip=True),
            'link': cols[col][2].find('noindex').find('a').get('href')
            })
        except IndexError:
            pass
    for result in results:
        result_string += f"🎮 В магазине {result['name_shop']} игру {name_of_game} можно купить за {result['price']}. \n\n👾Ссылка на магазин: {result['link']}\n\n"
    return result_string

