import requests
import time
from bs4 import BeautifulSoup


def get_one_page(url, headers):
    """获取url页面内容"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    """分析html代码，将需要的信息生成元组，返回生成器"""
    soup = BeautifulSoup(html, 'lxml')
    index = get_list_by_css(soup, ".board-index")
    img_src = get_list_by_css(soup, ".board-img", "data-src")
    film_name = get_list_by_css(soup, ".name")
    star = get_list_by_css(soup, ".star")
    release_time = get_list_by_css(soup, ".releasetime")
    score1 = get_list_by_css(soup, ".integer")
    score2 = get_list_by_css(soup, ".fraction")
    for i in range(len(index)):
        yield (index[i], img_src[i], film_name[i].strip(), star[i].strip(),
               release_time[i].strip(), score1[i] + score2[i])


def get_list_by_css(soup, css, attr=None):
    """从bs对象里获取指定css选择器的所有元素的相应内容，并以列表形式返回"""
    if attr is not None:
        the_list = [item.attrs[attr] for item in soup.select(css)]
    else:
        the_list = [item.string for item in soup.select(css)]
    return the_list


def write_to_file(item):
    with open('./spider/save/maoyan.txt', 'a', encoding='utf-8') as f:
        f.writelines(x + ' ' for x in item)
        f.write('\n')


def main(page_no, headers):
    url = 'http://maoyan.com/board/4?offset=%s' % page_no
    html = get_one_page(url, headers)
    for item in get_data(html):
        write_to_file(item)
        # print(item, type(item))


if __name__ == "__main__":
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36' +
        ' (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }

    with open('./spider/save/maoyan.txt', 'w', encoding='utf-8') as f:
        f.write('')
    for page_no in range(10):
        main(page_no * 10, headers)
        print('==============finish page %s=====================' % page_no)
        time.sleep(1)
