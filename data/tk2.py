import tkinter as tk
from backend import get_poet

class PoetQueryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("你的孩子是哪位诗人的转世")
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.master, text="你的孩子的名字是:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.dynasty_label = tk.Label(self.master, text="你喜欢的朝代:")
        self.dynasty_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.dynasty_entry = tk.Entry(self.master)
        self.dynasty_entry.grid(row=1, column=1, padx=10, pady=10)

        self.birth_date_label = tk.Label(self.master, text="你的孩子的出生日期 (年 月 日):")
        self.birth_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.birth_date_entry = tk.Entry(self.master)
        self.birth_date_entry.grid(row=2, column=1, padx=10, pady=10)

        self.province_label = tk.Label(self.master, text="孩子出生的省份:")
        self.province_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.province_entry = tk.Entry(self.master)
        self.province_entry.grid(row=3, column=1, padx=10, pady=10)

        self.season_label = tk.Label(self.master, text="你喜欢的季节:")
        self.season_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.season_entry = tk.Entry(self.master)
        self.season_entry.grid(row=4, column=1, padx=10, pady=10)

        self.romantic_label = tk.Label(self.master, text="你喜欢的文学流派:")
        self.romantic_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.romantic_entry = tk.Entry(self.master)
        self.romantic_entry.grid(row=5, column=1, padx=10, pady=10)

        self.submit_btn = tk.Button(self.master, text="提交", command=self.on_submit)
        self.submit_btn.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(self.master, height=10, wrap="word")
        self.result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.master.grid_rowconfigure(7, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def on_submit(self):
        name = self.name_entry.get()
        dynasty = self.dynasty_entry.get()
        birth_date = self.birth_date_entry.get().split()
        year, month, day = (birth_date + ['None', 'None'])[:3]
        province = self.province_entry.get()
        season = self.season_entry.get()
        romantic = self.romantic_entry.get()
        
        results = get_poet(name, dynasty, year, month, day, province, season, romantic)
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, results)

def launch_app():
    root = tk.Tk()
    app = PoetQueryApp(root)
    root.mainloop()

if __name__ == "__main__":
    launch_app()
