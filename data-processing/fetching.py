import requests
import re
import pickle
from bs4 import BeautifulSoup
import re

class Poet:
    def __init__(self, author, dynasty):
        self.author = author
        self.dynasty = dynasty

    def __eq__(self, other):
        if isinstance(other, Poet):
            return self.author == other.author and self.dynasty == other.dynasty
        return False

    def __hash__(self):
        return hash((self.author, self.dynasty))
    
class PoetPlus:
    def __init__(self, author, dynasty, birth_death, zi, hao, birth_place, style):
        self.author = author
        self.dynasty = dynasty
        self.birth_death = birth_death
        self.zi = zi
        self.hao = hao
        self.birth_place = birth_place
        self.style = style

    def __eq__(self, other):
        if isinstance(other, Poet):
            return self.author == other.author and self.dynasty == other.dynasty
        return False

    def __hash__(self):
        return hash((self.author, self.dynasty))



def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML content: {e}")
        return None


def generate_poet_urls(author_set):
    poet_url = []  # 存储生成的URL字符串的列表
    for item in author_set:
        url = f"https://zh.wikipedia.org/wiki/{item.author}"
        poet_url.append(url)
    return poet_url



def fetch(poet):
    myurl = f"https://baike.baidu.com/item/{poet.author}"
    r = requests.get(myurl, timeout=5)
    if r is None:
        return
    soup = BeautifulSoup(r.content, 'html.parser')
    # 找到包含作者信息的 meta 标签
    description_meta = soup.find('meta', {'name': 'description'})

    # 如果找到了 meta 标签，则提取其 content 属性值
    if description_meta:
        author_info = description_meta['content']
    else:
        return
        #print(author_info)
        #print("未找到作者信息")
    # 诗人名字
    name_search = re.search(r'^(.*?)（', author_info)
    name = name_search.group(1) if name_search else None

    # 诗人生卒新信息
    birth_death_search = re.search(r'（(.*?)）', author_info)
    birth_death = birth_death_search.group(1) if birth_death_search else None

    # 字
    zi_search = re.search(r'，字(.*?)，', author_info)
    zi = zi_search.group(1) if zi_search else None

    # 号
    hao_search = re.search(r'，号(.*?)，', author_info)
    hao = hao_search.group(1) if hao_search else None

    # 出生地
    birth_place_search = re.search(r'，出生于(.*?)，', author_info)
    birth_place = birth_place_search.group(1) if birth_place_search else None

    # 风格
    style_search = re.search(r'(\w{2}主义)诗人', author_info)
    style = style_search.group(1) if style_search else None

    if name is None and birth_death is None and zi is None and hao is None and birth_place is None and style is None:
        return
    
    poet_plus = PoetPlus(poet.author, poet.dynasty, birth_death, zi, hao, birth_place, style)
    author_info_list.append(poet_plus)
    pickle.dump(author_info_list, open('author_info.pkl', 'wb'))

    with open('output1.txt', 'a') as f:
        print(f"诗人名（原来的）: {poet.author}", file=f)
        print(f"诗人名字: {name}", file=f)
        print(f"诗人生卒信息: {birth_death}", file=f)
        print(f"字: {zi}", file=f)
        print(f"号: {hao}", file=f)
        print(f"出生地: {birth_place}", file=f)
        print(f"风格: {style}", file=f)

authors_set = set()
author_info_list = []

if __name__ == "__main__":
    with open('authors_set.pkl', 'rb') as f:
        authors_set = pickle.load(f)
    #poet_url = generate_poet_urls(authors_set)

    cnt = 0

    for poet in authors_set:
        # cnt += 1
        # if(cnt == 400):
        #     break
        fetch(poet)

    #fetch("杜甫")


