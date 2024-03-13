import pickle
import os


class PoetPlus:
    def __init__(self, author, dynasty, birth_death, zi, hao, birth_place, style):
        self.author = author
        self.dynasty = dynasty
        self.birth_death = birth_death
        self.zi = zi
        self.hao = hao
        self.birth_place = birth_place
        self.style = style

poet_list = []

if __name__ == "__main__":
    with open('output.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 8):  # Each poet's information spans 8 lines
            author = lines[i+2].split(': ')[1].strip()
            dynasty = lines[i+1].split(': ')[1].strip()
            birth_death = lines[i+3].split(': ')[1].strip()
            zi = lines[i+4].split(': ')[1].strip()
            hao = lines[i+5].split(': ')[1].strip()
            birth_place = lines[i+6].split(': ')[1].strip()
            style = lines[i+7].split(': ')[1].strip()
            poet = PoetPlus(author, dynasty, birth_death, zi, hao, birth_place, style)
            poet_list.append(poet)
        
    with open('output.pkl', 'wb') as f:
        pickle.dump(poet_list, f)