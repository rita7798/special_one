# coding: utf-8


import json
import urllib.request
import re
import key
from collections import OrderedDict


def posts():
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-112510789&count=10&v=5.73&access_token={}'.format(key.access))
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    data = json.loads(html) 
    for i in range(10):
        with open ('corpora.txt', 'a', encoding='utf-8') as f:
            f.write(data["response"]["items"][i]['text'])


def dictionary():
    punct = []
    d = {}
    with open ('corpora.txt', 'r', encoding='utf-8') as f:
        text = f.read().lower()
        new_text = re.sub('[\.\?\!…\(\)\-\—\,\"–]', ' ', text)
    for word in new_text.split():
        if word not in d:
            d.update({word:1})
        else:
            key = word
            d.update({key:d[key]+1})
    d = OrderedDict(sorted(d.items(), key=lambda t: t[0]))


def main():
    posts()
    dictionary()


if __name__ == '__main__':
    main()

