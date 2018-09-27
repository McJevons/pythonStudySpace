import requests
import re
from bs4 import BeautifulSoup


def get_html(url, headers):
    req = requests.get(url, headers=headers)
    return req.text


def get_items(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.select('.subject-item')


def get_data(items):
    for item in items:
        # title = re.sub('\s*', '', item.select('.info h2 a')[0].text)
        # title = re.sub('\s*', '', item.h2.a.text)
        title = item.h2.a['title']
        url = item.h2.a['href']
        # 可能存在没有评分的情况，不一定能取得rating_nums
        star = item.find(class_='rating_nums')
        star = star.text if star else '--'
        price = re.sub('\s*', '', item.find(class_='pub').text)
        try:
            price = re.search('\d+\.{0,1}\d*元{0,1}$', price).group(0)
        except:
            price = '--'
        print(star, price, title, url)


def get_tag():
    '''获取查询关键词'''
    while True:
        tag = input('Please input the tag:')
        if tag.strip() == '':
            print('Wrong input!')
        else:
            return tag


if __name__ == '__main__':
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }

    tag = get_tag()

    for page in range(3):
        page_no = page * 20
        url = 'https://book.douban.com/tag/%s?start=%d&type=T' % (tag, page_no)
        html = get_html(url, headers)
        items = get_items(html)
        get_data(items)
