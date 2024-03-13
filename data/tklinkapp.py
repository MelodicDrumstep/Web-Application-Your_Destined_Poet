import tkinter as tk
from tkinter import simpledialog
from backend import get_poet

# 创建一个简单的 Tkinter 应用界面来替代 Flask 的 Web 界面
def launch_app():
    root = tk.Tk()
    root.title("诗人查询系统")
    root.geometry("400x600")

    # 创建一个函数来处理表单提交
    def on_submit():
        # 获取输入值
        name = name_entry.get()
        dynasty = dynasty_entry.get()
        birth_date = birth_date_entry.get().split()
        year, month, day = (birth_date + ['None', 'None'])[:3]  # 确保年月日都有值
        province = province_entry.get()
        season = season_entry.get()
        romantic = romantic_entry.get()
        
        # 调用主要逻辑
        results = get_poet(name, dynasty, year, month, day, province, season, romantic)
        
        # 显示结果
        result_label.config(text=results)
    
    # 创建输入字段
    name_entry = tk.Entry(root)
    name_entry.pack()
    dynasty_entry = tk.Entry(root)
    dynasty_entry.pack()
    birth_date_entry = tk.Entry(root)
    birth_date_entry.pack()
    province_entry = tk.Entry(root)
    province_entry.pack()
    season_entry = tk.Entry(root)
    season_entry.pack()
    romantic_entry = tk.Entry(root)
    romantic_entry.pack()
    
    # 提交按钮
    submit_btn = tk.Button(root, text="提交", command=on_submit)
    submit_btn.pack()
    
    # 结果显示标签
    result_label = tk.Label(root, text="", wraplength=400)
    result_label.pack()
    
    # 启动 Tkinter 事件循环
    root.mainloop()

if __name__ == '__main__':
    launch_app()
