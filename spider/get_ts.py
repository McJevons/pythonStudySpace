import requests
import os


def save_ts_files(path):
    '''下载并保存文件'''
    max_file_num = 0  # 有效的最大文件序号
    for filename in filename_list:
        ts_file = requests.get(url + filename)
        if str(ts_file.status_code) == '404':
            break
        else:
            print('%s finish!' % filename)
            max_file_num += 1
        with open(os.path.join(path, filename), 'wb') as f:
            f.write(ts_file.content)
    return max_file_num


def get_fold_path():
    '''建立目录，并返回路径'''
    # 先获取本py文件的绝对路径，再获取文件所在文件夹路径
    cwd = os.path.dirname(os.path.abspath(__file__))
    fold_path = os.path.join(cwd, 'av')  # 文件保存路径为本文件所在目录下的AV目录
    if not os.path.exists(fold_path):
        os.mkdir(fold_path)
    return fold_path


def combine_ts(path, filename_list, save_filename, max_file_num):
    '''合并文件'''
    os.chdir(path)
    shell = 'copy /b ' + '+'.join(
        filename_list[:max_file_num]) + ' ' + save_filename
    print(shell)
    print('开始合并文件！')
    os.system(shell)


if __name__ == '__main__':
    url = 'http://www.91gxflvip.com:2100/20180809/UljdSVF8/490kb/hls/'
    save_filename = 'papapa.ts'

    # 生成文件名列表
    filename_list = [
        'JRrg1xO5057%s.ts' % ('00' + str(i))
        if i < 10 else 'JRrg1xO5057%s.ts' % ('0' + str(i))
        if i < 100 else 'JRrg1xO5057%s.ts' % str(i) for i in range(999)
    ]

    path = get_fold_path()

    max_file_num = save_ts_files(path)
    print('下载完成！')

    combine_ts(path, filename_list, save_filename, max_file_num)
    print('任务完成，请欣赏%s' % (os.path.join(path, save_filename)))
