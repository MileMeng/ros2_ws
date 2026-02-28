import threading
import requests
import os
from functools import wraps


# 装饰器：给回调函数增加日志功能
def download_logger(func):
    """
    装饰器：增强下载回调函数
    - 打印线程信息
    - 打印保存路径
    - 打印内容长度
    """
    @wraps(func)
    def wrapper(filename, content):
        print(f'线程：{threading.get_ident()} 回调开始')

        # 调用原始回调函数
        result = func(filename, content)

        print(f'线程：{threading.get_ident()} 下载完成')
        print(f'保存路径：{os.path.abspath(filename)}')
        print(f'内容长度：{len(content)}，前5个字符：{content[:5]}')
        print('-' * 50)

        return result

    return wrapper


class Download:
    def download(self, url, filename, callback):
        print(f'线程：{threading.get_ident()} 开始下载：{url}')
        response = requests.get(url)
        response.encoding = 'utf-8'

        # 下载完成后，调用回调函数
        callback(filename, response.text)

    def start_download(self, url, filename, callback):
        thread = threading.Thread(
            target=self.download,
            args=(url, filename, callback)
        )
        thread.start()



@download_logger
def word_count_callback(filename, content):
    """
    回调函数：只负责业务逻辑
    这里的业务逻辑是：保存文件
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)



def main():
    downloader = Download()

    url1 = 'https://www.gutenberg.org/files/1342/1342-0.txt'
    url2 = 'https://www.gutenberg.org/files/11/11-0.txt'

    filename1 = 'pride_and_prejudice.txt'
    filename2 = 'alice_in_wonderland.txt'

    downloader.start_download(url1, filename1, word_count_callback)
    downloader.start_download(url2, filename2, word_count_callback)


if __name__ == '__main__':
    main()
