import requests
import time
from lxml import etree

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36' +
    ' (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}


def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    html = etree.HTML(html)
    index = html.xpath('//dd//i[contains(@class,"board-index")]/text()')
    img_src = html.xpath('//dd/a/img/@data-src')
    film_name = html.xpath('//dd//p[@class="name"]/a/text()')
    star = html.xpath('//dd//p[@class="star"]/text()')
    release_time = html.xpath('//dd//p[@class="releasetime"]/text()')
    score1 = html.xpath('//dd//p[@class="score"]/i[1]/text()')
    score2 = html.xpath('//dd//p[@class="score"]/i[2]/text()')
    for i in range(10):
        yield (index[i], img_src[i], film_name[i].strip(), star[i].strip(),
               release_time[i].strip(), score1[i] + score2[i])


def main(page_no):
    url = 'http://maoyan.com/board/4?offset=%s' % page_no
    html = get_one_page(url)
    # result = get_data(html)
    for item in get_data(html):
        write_to_file(item)


def write_to_file(item):
    with open('./spider/save/maoyan.txt', 'a', encoding='utf-8') as f:
        f.writelines(x + ' ' for x in item)
        f.write('\n')
        # f.write(str(item) + '\n')


with open('./spider/save/maoyan.txt', 'w', encoding='utf-8') as f:
    f.write('')

for page_no in range(1):
    main(page_no * 10)
    print('==============finish page %s=====================' % page_no)
    time.sleep(10)
    