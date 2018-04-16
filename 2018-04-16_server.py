# coding: utf-8


import json
import urllib.request
import re
import key


COUNT = 10

def posts():
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-112510789&count={}&v=5.73&access_token={}'.format(COUNT, key.access))
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    data = json.loads(html) 
    for i in range(COUNT):
        with open ('corp.txt', 'a', encoding='utf-8') as f:
            f.write(data["response"]["items"][i]['text'])


def dictionary():
    d = {}
    with open ('corp.txt', 'r', encoding='utf-8') as f:
        text = f.read().lower()
        new_text = re.sub('[\.\?\!…\(\)\-\—\,\"–]', ' ', text)
    for word in new_text.split():
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    with open ('dictionary.tsv', 'a', encoding='utf-8') as f:
        for k in sorted(d, key = d.get, reverse=True):
            f.write("{}\t{}".format(k,d[k]) + "\n")


def main():
    posts()
    dictionary()


if __name__ == '__main__':
    main()
