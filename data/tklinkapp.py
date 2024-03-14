import tkinter as tk
from tkinter.font import Font
from backend import get_poet

class PoetQueryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("你的天命诗人查询系统")
        self.master.geometry("800x600")

        self.pages = [
            ("名字", "name"),
            ("朝代", "dynasty"),
            ("出生日期 (年/月/日)", "birth_date"),
            ("省份", "province"),
            ("季节", "season"),
            ("文学流派", "romantic")
        ]
        self.current_page = 0
        self.answers = {}

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text=self.pages[self.current_page][0], font=("Arial", 20))
        self.label.pack(side="top", pady=50)
        
        # 使用StringVar跟踪输入的内容
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.master, textvariable=self.entry_var, font=("Arial", 20))
        self.entry.pack(side="top", pady=10)

        self.submit_btn = tk.Button(self.master, text="下一步", font=("Arial", 20), command=self.on_submit)
        self.submit_btn.pack(side="top", pady=10)

    def on_submit(self):
        self.answers[self.pages[self.current_page][1]] = self.entry_var.get()
        self.current_page += 1
        if self.current_page < len(self.pages):
            self.label.config(text=self.pages[self.current_page][0])
            self.entry_var.set("")  # 清空输入框
        else:
            self.show_results()

    def show_results(self):
        result_window = tk.Toplevel(self.master)
        result_window.title("查询结果")
        result_text = tk.Text(result_window, font=("Arial", 20))
        results = get_poet(**self.answers)
        result_text.insert(tk.END, results)
        result_text.pack(expand=True, fill="both", padx=20, pady=20)
        result_text.tag_configure("center", justify='center')
        result_text.tag_add("center", "1.0", "end")

def launch_app():
    root = tk.Tk()
    app = PoetQueryApp(root)
    root.mainloop()

if __name__ == "__main__":
    launch_app()
