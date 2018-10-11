import requests
import re
import os
import json
import csv
from bs4 import BeautifulSoup


def get_html(url, headers):
    '''获取页面html'''
    response = requests.get(url, headers=headers)
    return response.text


def get_items(html, str_type):
    '''获取页面中所需的所有条目'''
    soup = BeautifulSoup(html, 'lxml')
    if str_type == 'book':
        items = soup.select('.subject-item')
    elif str_type == 'movie':
        items = soup.select('.item')
    return items


def make_list(items, data_list, str_type):
    '''根据类型从每个条目中取得需要的数据，添加至list'''
    if str_type == 'book':
        make_book_list(items, data_list)
    elif str_type == 'movie':
        make_movie_list(items, data_list)


def get_star(item):
    # 可能存在没有评分的情况，不一定能取得rating_nums
    star = item.find(class_='rating_nums')
    if star:
        if star.text.strip() == '':
            return '--'
        else:
            return star.text
    else:
        return '--'


def make_movie_list(items, data_list):
    for item in items:
        title = item.td.a['title']
        url = item.td.a['href']
        star = get_star(item)
        try:
            # 只获取第一个日期
            year = re.match(
                '\d{4}-{1}\d{2}-{1}\d{2}',
                item.find(class_='pl').text).group(0)
        except Exception:
            year = '--'
        data_list.append([star, year, title, url])


def make_book_list(items, data_list):
    for item in items:
        title = item.h2.a['title']
        url = item.h2.a['href']
        star = get_star(item)
        price = re.sub('\s*', '', item.find(class_='pub').text)
        try:
            price = re.search('\d+\.{0,1}\d*元{0,1}$', price).group(0)
        except Exception:
            price = '--'
        data_list.append([star, price, title, url])


def get_tag():
    '''获取要查询的标签关键词'''
    while True:
        tag = input('请输入标签:')
        if tag.strip() == '':
            print('输入有误，请重新输入！')
        else:
            return tag


def get_type():
    '''获取类型，1为书籍，2为电影'''
    while True:
        type_id = input('请选择类型：1.书籍 2.电影')
        if type_id == '1':
            return 'book'
        elif type_id == '2':
            return 'movie'
        else:
            print('错误的选择，请重新选择！')


def get_filetype():
    '''获取保存的文件类型'''
    while True:
        type_id = input('请选择保存的文件类型：1.文本格式 2.json格式 3.csv格式')
        if type_id == '1':
            return 'txt'
        elif type_id == '2':
            return 'json'
        elif type_id == '3':
            return 'csv'
        else:
            print('错误的选择，请重新选择！')


def save_file(data_list, keys, tag, str_type):
    file_type = get_filetype()
    file_name = 'douban-%s-%s.%s' % (str_type, tag, file_type)
    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)) + '\\save\\', file_name)
    if file_type == 'txt':
        save_txt(file_path, data_list)
    elif file_type == 'json':
        save_json(file_path, data_list, keys)
    elif file_type == 'csv':
        save_csv(file_path, data_list, keys)
    return file_path


def save_txt(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(' '.join(item))
            file.write('\n')


def save_json(file_path, data_list, keys):
    with open(file_path, 'w', encoding='utf-8') as file:
        # 将data_list里的每个list元素与keys列表进行zip，并强制转换成dict类型
        # 通过遍历data_list建立列表生成器，其中每个元素是一个dict
        list_dict = [dict(zip(keys, item)) for item in data_list]
        # 列表转为json，并写入文件中，设置缩进为2，支持中文
        file.write(json.dumps(list_dict, indent=2, ensure_ascii=False))


def save_csv(file_path, data_list, keys):
    print(data_list)
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(keys)
        writer.writerows(data_list)


def operate_pages(tag, str_type, data_list, headers):
    '''分析处理每个页面'''
    has_data = False  # 查询结果标志

    # range为页数，每页20条记录
    for page in range(3):
        page_no = page * 20
        url = 'https://%s.douban.com/tag/%s?start=%d&type=T' % (str_type, tag,
                                                                page_no)
        html = get_html(url, headers)
        items = get_items(html, str_type)

        # items可能为none，表示该页面没有所需获取的条目，中断操作
        if items:
            make_list(items, data_list, str_type)
            has_data = True
        else:
            print('没有和标签%s相关的内容！' % tag)
            print(url)
            return has_data
    return has_data


def main():
    data_list = []

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    # 获取查询条件
    tag = get_tag()
    str_type = get_type()
    # 列名列表，书籍和电影有区别
    keys = ['评分', '价格', '书名',
            '链接'] if str_type == 'book' else ['评分', '上映日期', '片名', '链接']
    has_data = operate_pages(tag, str_type, data_list, headers)

    if has_data:
        print("数据获取完成！")
        # data_list数据根据分数进行排序
        data_list.sort(key=lambda x: x[0], reverse=True)
        file_name = save_file(data_list, keys, tag, str_type)
        print('查询结果已保存：%s' % file_name)


if __name__ == '__main__':
    main()
