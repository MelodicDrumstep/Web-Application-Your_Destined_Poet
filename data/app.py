# app.py
from flask import Flask, request, render_template_string
from backend import calculate_score, get_poet

app = Flask(__name__)

# Flask路由处理
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 从表单获取数据
        name = request.form.get('name')
        gender = request.form.get('gender')  # 此例中未使用
        dynasty = request.form.get('dynasty')
        birth_date = request.form.get('birth_date').split()
        if(len(birth_date) == 3):
            year = (birth_date[0])
            month = (birth_date[1])
            day = (birth_date[2])
        elif (len(birth_date) == 2):
            year = (birth_date[0])
            month = (birth_date[1])
            day = 'None'
        else:
            year = (birth_date[0])
            month = 'None'
            day = 'None'
        province = request.form.get('province')
        season = request.form.get('season')
        romantic = request.form.get('romantic')
        
        # 调用主要逻辑
        results = get_poet(name, dynasty, year, month, day, province, season, romantic)
    
        # 在渲染模板之前转义或删除HTML标签
        results = results.replace("<strong>", "").replace("</strong>", "")
        results = results.replace("<br>", "\n")

        return render_template_string('''
    <html>
        <body>
            <div style="white-space: pre-wrap;">{{ results }}</div>
        </body>
    </html>
    ''', results=results)
        
    # 显示输入表单
    return render_template_string('''<html>
        <body>
            <h2>输入信息</h2>
            <form method="post">
                名字: <input type="text" name="name"><br>
                性别: <input type="text" name="gender"><br>
                喜欢的朝代: <input type="text" name="dynasty"><br>
                出生日期 (年/月/日): <input type="text" name="birth_date"><br>
                省份: <input type="text" name="province"><br>
                喜欢的季节: <input type="text" name="season"><br>
                喜欢的文学流派: <input type="text" name="romantic"><br>
                <input type="submit" value="提交">
            </form>
        </body>
    </html>''')

if __name__ == '__main__':
    app.run(debug=True)