import requests
import re
from bs4 import BeautifulSoup


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML content: {e}")
        return None


def generate_poet_urls():
    poet_url = []  # 存储生成的URL字符串的列表
    for i in range(1, 30000):
        url = f"https://www.shicimingju.com/chaxun/zuozhe/{i}.html"
        poet_url.append(url)
    return poet_url


def fetch_poet(url):
    poet = {
        "name": "",
    }
    soup = BeautifulSoup(fetch_html(url), 'html.parser')
    poet_name_tag = soup.find('h1', text=re.compile(r'「.*?」'))
    if poet_name_tag:
        poet["name"] = poet_name_tag.text.strip().replace("\n", "")
    return poet


if __name__ == "__main__":
    poet_url = generate_poet_urls()
    res_list = []
    for url in poet_url:
        poet = fetch_poet(url)
        print(poet)

