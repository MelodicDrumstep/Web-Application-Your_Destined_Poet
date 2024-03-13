import pickle
from Levenshtein import distance
from pypinyin import lazy_pinyin
import os
import sys

NUM = 0.5

class PoetPlus:
    def __init__(self, author, dynasty, birth_death, zi, hao, birth_place, style):
        self.author = author
        self.dynasty = dynasty
        self.birth_death = birth_death
        self.zi = zi
        self.hao = hao
        self.birth_place = birth_place
        self.style = style

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == 'PoetPlus':
            from poetplus import PoetPlus
            return PoetPlus
        return super().find_class(module, name)

def calculate_score(item, dynasty, name, year, month, day, province, season, romantic):
    scores = {}
    if item.dynasty != 'None':
        scores['dynasty'] = 1 / (distance(dynasty, item.dynasty) + NUM)* 5
    else:
        scores['dynasty'] = 0
    scores['author'] = 1 / (distance(name, item.author) + NUM) * 10
    if name[0] == item.author[0]:
        scores['author'] += 6

    user_name = lazy_pinyin(name)
    poet_name = lazy_pinyin(item.author)
    
    for i in range(len(user_name)):
        for j in range(len(poet_name)):
            if user_name[i] == poet_name[j]:
                scores['author'] += 3 * (i + j + 1)

    if item.zi != 'None':
        scores['zi'] = 1 / (distance(name, item.zi) + NUM) * 3
        for i in range(len(user_name)):
            for j in range(len(poet_name)):
                if user_name[i] == poet_name[j]:
                    scores['zi'] += 1 * (i + j + 1)
    else:
        scores['zi'] = 0
    if item.hao != 'None':
        scores['hao'] = 1 / (distance(name, item.hao) + NUM) * 2  
        for i in range(len(user_name)):
            for j in range(len(poet_name)):
                if user_name[i] == poet_name[j]:
                    scores['hao'] += 1 * (i + j + 1)
    else:
        scores['hao'] = 0
    if item.birth_death != 'None' and year != 'None':
        scores['birth_year'] = 3 if (int(year) - int(item.birth_death)) % 100 == 0 else 0
    else:
        scores['birth_year'] = 0
    if item.birth_death != 'None' and month != 'None' and day != 'None':
        scores['birth_month'] = 3 if (int(item.birth_death) - int(month)) % 100 == 0 else 0
    else:
        scores['birth_month'] = 0
    if item.birth_death != 'None' and day != 'None':
        scores['birth_day'] = 3 if (int(item.birth_death) - int(day)) % 100 == 0 else 0
    else:
        scores['birth_day'] = 0
    if item.birth_place != 'None':
        scores['birth_place'] = 1 / (distance(province, item.birth_place) + NUM)
        scores['season'] = 1 / (distance(season, item.birth_place) + NUM)
    else:
        scores['birth_place'] = 0

    scores['name_season'] = 1 / (distance(season, item.author) + NUM)
    if item.style != 'None':
        scores['style'] = 1 / (distance(romantic, item.style) + NUM)
    else:
        scores['style'] = 0
    return scores


def get_poet(name, dynasty, year, month, day, province, season, romantic):

    print('PoetPlus:', PoetPlus)  # Check if PoetPlus is recognized

    poet = None
    max_score = 0
    details = []  # 存储最终的详细信息

    # 检测是否运行在打包后的环境
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    # 根据运行环境设置 output.pkl 的路径
    output_pkl_path = os.path.join(application_path, 'output.pkl')

    # 使用 output_pkl_path 来加载文件
    with open(output_pkl_path, 'rb') as f:
        data = CustomUnpickler(f).load()

    for item in data:
        scores = calculate_score(item, dynasty, name, year, month, day, province, season, romantic)
        score = sum(scores.values())
        #details.append(f"你的孩子和{item.author}的相似度是{score:.2f}。")
        if score > max_score:
            max_score = score
            poet = item

    if poet:
        details.append(f"<strong>恭喜你，你的孩子是{poet.author}的转世。</strong>")
        scores = calculate_score(poet, dynasty, name, year, month, day, province, season, romantic)
        if scores['dynasty'] > 3:
            details.append(f"他的朝代是{poet.dynasty}，正如你所愿。")
        if scores['author'] > 3:
            details.append(f"他的名字是{poet.author}。")
            if scores['zi'] > 2:
                details.append(f"他的字是{poet.zi}。")
                if scores['hao'] > 1.3:
                    details.append(f"他的号是{poet.hao}。")
            details.append(f"和你给孩子取的名字 '{name}' 十分相似。")  
        if scores['birth_year'] == 3:
            years_apart = abs(int(year) - int(poet.birth_death)) // 100
            details.append(f"他的出生年是{poet.birth_death}，正好和你的孩子的出生年相隔了{years_apart}百年。")
        if scores['style'] > 0.5:
            details.append(f"他的诗词风格是{poet.style}，你们有相似的品味。")
    else:
        details.append("未能找到匹配的诗人。")

    # 将详细信息列表转换为HTML格式的字符串
    return '<br>'.join(details)


# if __name__ == "__main__":
#     with open('output.pkl', 'rb') as f:
#         data = pickle.load(f)

#     name = input("请为你的孩子编写一个名字")

#     gender = input("Ta 是男生还是女生")

#     dynasty = input("你喜欢唐朝还是宋朝")

#     year, month, day = input("Ta 的出生年 / 月/ 日是 :").split()

#     province = input("Ta 来自中国哪个省份 : ")

#     season = input("你最喜欢哪个季节 :")

#     romantic = input("你喜欢浪漫主义还是现实主义 :")

#     get_poet()

    