import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    req = requests.get(url, headers=headers)
    return req.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # tmp=soup.select('div.info h2 a')
    # title = [re.sub('\s*', '', x.text) for x in tmp]
    items = soup.select('.subject-item')
    for item in items:
        title = re.sub('\s*', '', item.select('.info h2 a')[0].text)
        star = item.find(class_='rating_nums')
        star = star.text if star else '--'
        price = re.sub('\s*', '', item.select('.pub')[0].text)
        price = re.search('[^/{1}]?\d+\.{0,1}\d*元{0,1}.?$', price).group(0)
        print(title, star, price)


if __name__ == '__main__':
    url = 'https://book.douban.com/tag/儿童文学'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    html = get_html(url)
    get_data(html)
