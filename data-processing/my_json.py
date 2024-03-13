import os
import json
import pickle

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


# 创建一个空的集合用于存储作者信息
authors_set = set()

# 打开文件并读取内容
for i in range(1, 300):
    file_path = f'../../chinese-poetry/全唐诗/poet.song.{i * 1000}.json'
    if not os.path.exists(file_path):
        #print(f'文件不存在: {file_path}')
        continue
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # 遍历每个 JSON 对象，提取作者信息
        for entry in data:
            author = entry.get('author')
            if author:
                authors_set.add(Poet(author, "宋"))

# 打开文件并读取内容
for i in range(1, 300):
    file_path = f'../../chinese-poetry/全唐诗/poet.tang.{i * 1000}.json'
    if not os.path.exists(file_path):
        #print(f'文件不存在: {file_path}')
        continue
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # 遍历每个 JSON 对象，提取作者信息
        for entry in data:
            author = entry.get('author')
            if author:
                authors_set.add(Poet(author, "唐"))

# # 打印集合中的作者信息
# print(authors_set.__sizeof__())
# for author in authors_set:
#     print(author.author, author.dynasty)
                
# Pickle the set and save it to a file
with open('authors_set.pkl', 'wb') as f:
    pickle.dump(authors_set, f)
