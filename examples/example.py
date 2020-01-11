import os
import sys
import requests

_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _dir)


def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    return r.text


def crawl(url, proxy):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies)
    return r.text


def main():
    proxy = get_proxy()
    html = crawl('http://docs.jinkan.org/docs/flask/', proxy)
    print(html)


if __name__ == '__main__':
    main()

