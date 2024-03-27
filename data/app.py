from flask import Flask, request, render_template_string, render_template, session
from backend import calculate_score, get_poet
import sys
import os

# 获取当前文件（app.py）的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取data的绝对路径
data_folder_path = os.path.dirname(current_file_path)

# 构建poem_gene的绝对路径
poem_folder_path = os.path.join(data_folder_path, 'poem_gene')
poet_folder_path = os.path.join(data_folder_path, 'poet_gene')

# 将poem_folder的路径添加到sys.path中
sys.path.append(poem_folder_path)
sys.path.append(poet_folder_path)

from sequential_generate import generate_with_start_str


from poet_generate import generate_poem_with_tile_and_poet

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # 设置会话密钥

# Flask路由处理
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/poet', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/poem', methods=['GET', 'POST'])
def poem():
    return render_template('poem.html')

@app.route('/poem/result', methods=['POST'])
def poem_result():
    if request.method == 'POST':
        str = request.form.get('keyword')
        results = generate_with_start_str(str)
        line1 = results[0]
        line2 = results[1]
        line3 = results[2]
        line4 = results[3]
        line5 = results[4]
        line6 = results[5]
        return render_template('poem_result.html', line1=line1, line2=line2, line3=line3, line4=line4, line5=line5, line6=line6)

@app.route('/poet/result/game')
def game():
    name = session.get('name', '')  # 从会话中获取名字数据
    results = session.get('results', '')
    rank = session.get('rank', '')
    return render_template('task3rd.html', results = results, name = name, rank = rank)
        
@app.route('/poet/result/game/result', methods=['POST'])
def compute_game():
    if request.method == 'POST':
        name = session.get('name', '')  # 从会话中获取名字数据
        title = request.form.get('title')
        result = generate_poem_with_tile_and_poet(title, name)
        return render_template('task3rd_result.html', result = result)

# 用于处理测试页面的路由
@app.route('/poet/result', methods=['POST'])
def test():
    if request.method == 'POST':
        # 处理表单提交的数据
        name = request.form.get('name')
        gender = request.form.get('gender')
        dynasty = request.form.get('dynasty')
        birth_date = request.form.get('birth_date')
        if(len(birth_date) == 3):
            year = birth_date[0]
            month = birth_date[1]
            day = birth_date[2]
        elif(len(birth_date) == 2):
            year = birth_date[0]
            month = birth_date[1]
            day = None
        elif(len(birth_date) == 1):
            year = birth_date[0]
            month = None
            day = None
        else:
            year = None
            month = None
            day = None
        province = request.form.get('province')
        season = request.form.get('season')
        romantic = request.form.get('romantic')

        # 调用后端逻辑
        results, name, rank = get_poet(name, dynasty, year, month, day, province, season, romantic)

        # 在渲染模板之前转义或删除HTML标签
        results = results.replace("<strong>", "").replace("</strong>", "")
        results = results.replace("<br>", "\n")

        session['name'] = name  # 将名字存储在会话中
        session['results'] = results
        session['rank'] = rank
        
        # 渲染结果并返回
        return render_template('poet_result.html', results=results, name=name, rank = rank)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
