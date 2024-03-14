from flask import Flask, request, render_template_string, render_template
from backend import calculate_score, get_poet

app = Flask(__name__)

# Flask路由处理
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# 用于处理测试页面的路由
@app.route('/test', methods=['POST'])
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
        
        # rank_class = ""
        # if rank == "稀有":
        #     rank_class = "rank-blue"
        # elif rank == "史诗":
        #     rank_class = "rank-purple"
        # else:
        #     rank_class = "rank-gold"

        # 渲染结果并返回
        return render_template('result.html', results=results, name=name, rank = rank)

if __name__ == '__main__':
    app.run(debug = False)
