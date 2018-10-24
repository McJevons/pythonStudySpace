import json
import os
from pyquery import PyQuery as pq
from docx import Document


def get_chapters(url):
    '''获取章节列表，包括各章节的标题，url，并预留正文空白'''
    doc = pq(url, encoding='gb2312')
    # 最后一项id=d999，非小说相关内容需排除，使用css的:not()方法排除
    chapters = [{
        'title': item.text(),
        'url': url + item.attr('href'),
        'content': ''
    } for item in doc('table.acss td.ccss a:not(#d999)').items()]
    return chapters


def insert_cotent_to_chapters(chapters):
    '''将正文内容插入章节列表中'''
    for chapter in chapters:
        content = get_content(chapter['url'])
        chapter['content'] = content
        print('%s 读取完毕！' % chapter['title'])


def get_content(url):
    '''获取正文内容'''
    # print(url)
    doc = pq(url, encoding='gb2312')
    content_item = doc('#content')
    content = content_item.text()
    return content


def save_file_txt(chapters):
    '''保存为txt文件'''
    with open('九阴九阳.txt', 'w', encoding='utf-8') as file:
        for chapter in chapters:
            file.write(chapter['title'] + '\n')
            file.write(chapter['content'] + '\n')
            file.write('\n\n\n===================================\n')
            print('%s 保存完毕！' % chapter['title'])


def save_file_docx(filename_json):
    '''保存为docx文件'''
    document = Document()
    document.add_heading('九阴九阳', 0)
    with open(filename_json, encoding='utf-8') as file:
        chapters = json.load(file)

    for chapter in chapters:
        document.add_heading(chapter['title'], 2)
        p = document.add_paragraph(chapter['content'])
        # p.paragraph_format.first_line_indent=2
        document.add_page_break()
        print('%s 保存完毕！' % chapter['title'])

    document.save('九阴九阳.docx')


def save_file_json(chapters):
    with open('九阴九阳.json', 'w', encoding='utf-8') as file:
        json.dump(chapters, file, ensure_ascii=False, indent=2)
    print('小说全部读取完毕，准备保存')


def main():
    filename_json = '九阴九阳.json'
    if not os.path.exists(filename_json):
        url = 'https://www.555zw.com/book/7/7509/'
        chapters = get_chapters(url)
        insert_cotent_to_chapters(chapters)
        save_file_json(chapters)

    # save_file_txt(chapters)
    save_file_docx(filename_json)
    print('小说全部保存完毕！')


if __name__ == '__main__':
    main()
