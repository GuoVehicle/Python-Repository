#-*-coding:utf-8-*-
'''
爬虫-今日头条图片
'''
__athaor__='vehicle guo'

import requests
from urllib.parse import urlencode
from requests.exceptions import  RequestException
def get_page_index(offset,keyword):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求失败')
        return None


def main():
    html=get_page_index(0,'街拍')
    print(html)

if __name__=='__main__':
    main()