import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    req = requests.get(url, headers=headers)
    return req.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    get_item(soup.select('.subject-item'))


def get_item(items):
    for item in items:
        # title = re.sub('\s*', '', item.select('.info h2 a')[0].text)
        title = re.sub('\s*', '', item.h2.a.text)
        # 可能存在没有评分的情况，不一定能取得rating_nums
        star = item.find(class_='rating_nums')
        star = star.text if star else '--'
        price = re.sub('\s*', '', item.find(class_='pub').text)
        price = re.search('\d+\.{0,1}\d*元{0,1}$', price).group(0)
        print(title, star, price)


if __name__ == '__main__':
    url = 'https://book.douban.com/tag/儿童文学?start=0&type=T'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    html = get_html(url)
    get_data(html)
