# -*- coding:utf-8 -*-
'''
爬虫-猫眼top100
'''
__author__='vehicle guo'

import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import re
import json
def get_one_page(url):
    try:
        session=requests.Session()
        headers = {'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        responses=session.get(url,headers=headers)
        if responses.status_code==200:
            return responses.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    ##re.s

    po=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?<p.*?releasetime">(.*?)</p>.*?</dd>',re.S)
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?<p.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()



def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__=='__main__':
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])
    # for i in range(10):
    #     main(i*10)