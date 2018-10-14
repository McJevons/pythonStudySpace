import urllib
import requests
import json


def get_json(url, headers):
    req = requests.get(url, headers=headers)
    # return req.json()
    str_json = json.dumps(req.json(), indent=2, ensure_ascii=False)
    return str_json


if __name__ == '__main__':
    page = 1
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304131831521082_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=%d' % page

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36',
        'X-Requested-With':
        'XMLHttpRequest'
    }

    str_json = get_json(url, headers)
    print(str_json)
