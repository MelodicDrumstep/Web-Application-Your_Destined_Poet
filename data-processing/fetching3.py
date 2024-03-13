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

def create_set():
    authors_set.add(Poet("杜甫", "唐"))
    authors_set.add(Poet("李白", "唐"))
    authors_set.add(Poet("白居易", "唐"))
    authors_set.add(Poet("王维", "唐"))
    authors_set.add(Poet("杜牧", "唐"))
    authors_set.add(Poet("孟浩然", "唐"))
    authors_set.add(Poet("王之涣", "唐"))
    authors_set.add(Poet("王昌龄", "唐"))
    authors_set.add(Poet("岑参", "唐"))
    authors_set.add(Poet("王勃", "唐"))
    authors_set.add(Poet("李商隐", "唐"))
    authors_set.add(Poet("李贺", "唐"))
    authors_set.add(Poet("李清照", "宋"))
    authors_set.add(Poet("苏轼", "宋"))
    authors_set.add(Poet("辛弃疾", "宋"))
    authors_set.add(Poet("欧阳修", "宋"))
    authors_set.add(Poet("陆游", "宋"))
    authors_set.add(Poet("柳宗元", "宋"))
    authors_set.add(Poet("范仲淹", "宋"))
    authors_set.add(Poet("杜审言", "唐"))
    authors_set.add(Poet("张籍", "唐"))
    authors_set.add(Poet("张祜", "唐"))
    authors_set.add(Poet("张九龄", "唐"))
    authors_set.add(Poet("张继", "唐"))
    authors_set.add(Poet("张志和", "唐"))
    authors_set.add(Poet("张神弼", "唐"))
    authors_set.add(Poet("张若虚", "唐"))
    authors_set.add(Poet("张泌", "唐"))
    # 添加更多唐宋诗人
    authors_set.add(Poet("韩愈", "唐"))
    authors_set.add(Poet("柳永", "宋"))
    authors_set.add(Poet("苏辙", "宋"))
    authors_set.add(Poet("黄庭坚", "宋"))
    authors_set.add(Poet("曾巩", "宋"))
    authors_set.add(Poet("秦观", "宋"))
    authors_set.add(Poet("周邦彦", "宋"))
    authors_set.add(Poet("梅尧臣", "唐"))
    authors_set.add(Poet("刘禹锡", "唐"))
    authors_set.add(Poet("韦应物", "唐"))
    authors_set.add(Poet("贾岛", "唐"))
    authors_set.add(Poet("司空图", "宋"))
    authors_set.add(Poet("邵雍", "宋"))
    authors_set.add(Poet("赵构", "宋"))
    authors_set.add(Poet("晏殊", "宋"))
    authors_set.add(Poet("晏几道", "宋"))
    authors_set.add(Poet("欧阳詹", "宋"))
    authors_set.add(Poet("曹雪芹", "清"))  # 虽然不是唐宋，但作为《红楼梦》的作者，也值得一提
    
    authors_set.add(Poet("钱起", "唐"))
    authors_set.add(Poet("孟郊", "唐"))
    authors_set.add(Poet("刘长卿", "唐"))
    authors_set.add(Poet("韩偓", "唐"))
    authors_set.add(Poet("许浑", "唐"))
    authors_set.add(Poet("贾岛", "唐"))
    authors_set.add(Poet("韩翃", "唐"))
    authors_set.add(Poet("皮日休", "唐"))
    authors_set.add(Poet("卢纶", "唐"))
    authors_set.add(Poet("杨万里", "宋"))
    authors_set.add(Poet("赵长卿", "宋"))
    authors_set.add(Poet("范成大", "宋"))
    authors_set.add(Poet("赵孟頫", "宋"))
    authors_set.add(Poet("姜夔", "宋"))
    authors_set.add(Poet("吴文英", "宋"))
    authors_set.add(Poet("魏了翁", "宋"))
    authors_set.add(Poet("辛稼轩", "宋"))
    authors_set.add(Poet("杨炯", "唐"))
    authors_set.add(Poet("骆宾王", "唐"))
    authors_set.add(Poet("刘辰翁", "宋"))
    authors_set.add(Poet("方岳", "宋"))
    authors_set.add(Poet("文天祥", "宋"))
    authors_set.add(Poet("陆象先", "宋"))
    authors_set.add(Poet("朱熹", "宋"))
    authors_set.add(Poet("黄机", "宋"))
    authors_set.add(Poet("吕本中", "宋"))
    authors_set.add(Poet("贺知章", "唐"))
    authors_set.add(Poet("司马光", "宋"))
    authors_set.add(Poet("韩愈", "唐"))
    authors_set.add(Poet("柳宗元", "唐"))
    authors_set.add(Poet("苏洵", "宋"))
    authors_set.add(Poet("苏辙", "宋"))
    authors_set.add(Poet("苏轼", "宋"))
    authors_set.add(Poet("黄庭坚", "宋"))
    authors_set.add(Poet("范仲淹", "宋"))
    authors_set.add(Poet("曾巩", "宋"))
    authors_set.add(Poet("欧阳修", "宋"))
    authors_set.add(Poet("李觏", "唐"))
    authors_set.add(Poet("韦庄", "唐"))
    authors_set.add(Poet("齐己", "唐"))
    authors_set.add(Poet("孟郊", "唐"))
    authors_set.add(Poet("元稹", "唐"))
    authors_set.add(Poet("白居易", "唐"))
    authors_set.add(Poet("刘禹锡", "唐"))
    authors_set.add(Poet("杜牧", "唐"))
    authors_set.add(Poet("杜甫", "唐"))
    authors_set.add(Poet("王维", "唐"))
    authors_set.add(Poet("王安石", "宋"))
    authors_set.add(Poet("李清照", "宋"))
    authors_set.add(Poet("辛弃疾", "宋"))
    authors_set.add(Poet("陆游", "宋"))
    authors_set.add(Poet("周敦颐", "宋"))
    authors_set.add(Poet("张载", "宋"))
    authors_set.add(Poet("程颢", "宋"))
    authors_set.add(Poet("程颐", "宋"))
    authors_set.add(Poet("朱熹", "宋"))
    authors_set.add(Poet("陈与义", "宋"))
    authors_set.add(Poet("韩冈", "宋"))
    authors_set.add(Poet("蔡襄", "宋"))
    authors_set.add(Poet("蔡确", "宋"))
    authors_set.add(Poet("苏颂", "宋"))
    authors_set.add(Poet("苏辙", "宋"))
    authors_set.add(Poet("曾布", "宋"))
    authors_set.add(Poet("赵构", "宋"))
    
    return authors_set


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
    pickle.dump(author_info_list, open('author_info_final.pkl', 'wb'))

    with open('output.txt', 'a') as f:
        print(f"诗人名（原来的）: {poet.author}", file=f)
        print(f"朝代: {poet.dynasty}", file=f)
        print(f"诗人名字: {name}", file=f)
        print(f"诗人生卒信息: {birth_death}", file=f)
        print(f"字: {zi}", file=f)
        print(f"号: {hao}", file=f)
        print(f"出生地: {birth_place}", file=f)
        print(f"风格: {style}", file=f)

authors_set = set()
author_info_list = []

if __name__ == "__main__":
    create_set()

    for poet in authors_set:
        # cnt += 1
        # if(cnt == 400):
        #     break
        fetch(poet)

    #fetch("杜甫")


