import requests

data = {
    'params':
    'Wzkwl1Kptzl1lnTmQDaGc/0lTd4GHaDBPJulNMDmAScDjvDGYUPigS25QTODc+cvOj/NPpbT1ljvq7g+8MKEE1UoQsn7YfEcg+xsbBPVJdqtxfCKnHwk/73r8IqMRaapm1/es2ktQfZQyEsbZxLDpx5aiI2YatkmoUYz59163wPolxTFjTujkvGhynfJgB4YRg4P/yuo6XcZyeKVq4q2oZx/ec4qdIFu4rPY2fbmQxLHKIbch97K8qEZUhGQLV1h4xTJkJzbg5Fgzpoo57cmTY70AxrriRF3AyU+60MFO/Y=',
    'encSecKey':
    '5d4f396c4f3266cbf6589dd191f107816670d8d6c9bd73172d3ea4baff0764faa4d1e56b13518d9404abe4d506005289c934520c3c0acd34da7fcca1f495ced500653d75759f93e6c2c3d2a8796c517885fa47e2adbe6fa580c4a26a942f5b42a7abfffa0edbeed9f1fc537f3ff43bb93f593ea02f5608c9b0be9cc13a6cfd42'
}
headers = {
    'Host':
    'music.163.com',
    'Connection':
    'keep-alive',
    'Content-Length':
    '598',
    'Pragma':
    'no-cache',
    'Cache-Control':
    'no-cache',
    'Origin':
    'https://music.163.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Content-Type':
    'application/x-www-form-urlencoded',
    'Accept':
    '*/*',
    'Referer':
    'https://music.163.com/',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cookie':
    '_ntes_nuid=8d2e821cb2814b10d569e45b041aaeec; _ngd_tid=g6KK6bkjw6FiTPfwyDdJZYof7K8x9Ukr; _iuqxldmzr_=32; vjuids=-4db5996d2.160a6d9ae0d.0.20f433db60337; usertrack=ezq0pVqbdeavbVefgXwLAg==; _ga=GA1.2.1091886399.1520137760; P_INFO=jewelcn@163.com|1527683386|2|study|00&99|shh&1524555029&kaola#shh&null#10#0#0|&0||jewelcn@163.com; __utma=187553192.1091886399.1520137760.1532271639.1532271639.1; __utmz=187553192.1532271639.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __oc_uuid=fecc6c40-8dbf-11e8-9930-d11777b61cca; vjlast=1514627772.1533431959.22; __f_=1535460153154; _ntes_nnid=8d2e821cb2814b10d569e45b041aaeec,1539349157800; vinfo_n_f_l_n3=9d40206be29d3a73.1.4.1514627771937.1535981736482.1539349352250; JSESSIONID-WYYY=YPzRTZ%2BknD1bUI3Zr6ni2r%2BGpS4y7vBrkdmX%5CFidoB2RuXRV1F5uQeE2jpn%2Ble9KQFcl%5ChDo7jZcooPcBwyKa3YeMgOqy9J%2FwyOijyQvKRfxD%5CHm%2FnUUA4B7dqVNW2v5ym%2F%5CyojUEs7s8D9YeI5%2FgcCp0%2Fw2UbtshruuNEji5jc6G9uZ%3A1539953909224; __utma=94650624.850192510.1507735571.1511786139.1539952110.4; __utmc=94650624; __utmz=94650624.1539952110.4.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=9KGm3qwjcjnu%2BNP3A9XH%2BU67GC%2BZOfACqNr3ck%2Fe3Ii%2FcfLkMyRaqtLPnYuX%2BynXvkpZJsxdJzpeZq8m%2BDKi0VE4QLtlA%2Bl6VXkicuzb8%2BIPa5FnAIp0WFBJ6S1SDBMdcng%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeadf452f6beaa99ec5386ac8ea6d45f979b9aaaf7488e8db884d35bf7b1abb8d12af0fea7c3b92afb95898eb27bb5b6ad8bed7fe992a0d4c4339c98e5b6b53d859de5bbce6e839dbfaff139a1b5e186b243abf1ad87cf618fa79e82f4809090a2baf854e9a7a2b9f561b4868694fb708aa6c086d97bfcb3e5a5ca63f48a8bd5d448b8b48fccef3e9688a58ae27fbabef8cccc5ca3eb8a8fc443b4f099a7c142f68dffb4c74a8fbcad8fe637e2a3; WM_TID=JFMWtLAic0FFQAUVFVJ4eJXhJaQ4oPHE; playerid=10136000; __utmb=94650624.5.10.1539952110'
}
req = requests.post(
    'https://music.163.com/weapi/search/suggest/web?csrf_token=',
    data=data,
    headers=headers)

print(req.text)
