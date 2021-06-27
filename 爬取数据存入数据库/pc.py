import requests
from lxml import etree
import json


def pc():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Referer': 'https: // www.cingta.com / school / ser'
    }
    # 获取网页源代码
    left = requests.get(url='https://www.cingta.com/school/api/area_list/', headers=headers)
    b = json.loads(left.content)["data"]["list"]
    for i in b:
        print(i)

    r = requests.get(url='https://www.cingta.com/school/api/name_uni_list/', headers=headers)
    a = json.loads(r.content)["data"]["list"]
    for i in a:
        print(i)
    return b, a


if __name__ == '__main__':
    pc()
