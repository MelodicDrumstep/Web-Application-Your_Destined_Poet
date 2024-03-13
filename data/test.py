import pickle

class PoetPlus:
    def __init__(self, author, dynasty, birth_death, zi, hao, birth_place, style):
        self.author = author
        self.dynasty = dynasty
        self.birth_death = birth_death
        self.zi = zi
        self.hao = hao
        self.birth_place = birth_place
        self.style = style

if __name__ == "__main__":
    with open('author_info.pkl', 'rb') as f:
        data = pickle.load(f)
        for author in data:
            print(author.author, author.dynasty, author.birth_death, author.zi, author.hao, author.birth_place, author.style)
            print()