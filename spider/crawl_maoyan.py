import requests
import re

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
    return result


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    result = get_data(html)
    for x in result:
        print(x[0], x[1], x[2], x[3], x[4], x[5] + x[6])


main()
