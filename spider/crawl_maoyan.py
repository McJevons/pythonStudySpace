import requests
import re
import time

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}


def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# <i\sclass="board-index.*?(\d.*?)">\d.*?</i>.*?<a\shref="(.*?)".*?title="(.*?)".*?class="star">\s*(.*?)\s*</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>
def get_data(html):
    result = re.findall(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)@.*?data-val.*?">(.*?)</a>.*?class="star">\s*(.*?)\s*</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        html, re.S)
    for x in result:
        yield (x[0], x[1], x[2], x[3], x[4], x[5] + x[6])


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

for page_no in range(3):
    main(page_no * 10)
    print('==============finish page %s=====================' % page_no)
    time.sleep(10)
