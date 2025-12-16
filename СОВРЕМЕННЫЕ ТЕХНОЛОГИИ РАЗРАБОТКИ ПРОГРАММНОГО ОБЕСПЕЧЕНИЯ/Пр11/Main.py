#Бондаренков Ум-252
#Практика 11

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Бондаренков Ум-252")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Калькулятор")

entry1 = tk.Entry(frame1, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

operation = ttk.Combobox(frame1, values=["+", "-", "*", "/"], width=5)
operation.grid(row=0, column=1, padx=5, pady=5)
operation.current(0)

entry2 = tk.Entry(frame1, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        messagebox.showinfo("Результат", f"Ответ: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

btn_calc = tk.Button(frame1, text="Вычислить", command=calculate)
btn_calc.grid(row=0, column=3, padx=5, pady=5)

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Выбор")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

chk1 = tk.Checkbutton(frame2, text="Первый", variable=var1)
chk2 = tk.Checkbutton(frame2, text="Второй", variable=var2)
chk3 = tk.Checkbutton(frame2, text="Третий", variable=var3)

chk1.pack(anchor="w")
chk2.pack(anchor="w")
chk3.pack(anchor="w")

def show_choice():
    choices = []
    if var1.get(): choices.append("первый")
    if var2.get(): choices.append("второй")
    if var3.get(): choices.append("третий")
    if choices:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showwarning("Выбор", "Ничего не выбрано!")

btn_choice = tk.Button(frame2, text="Показать выбор", command=show_choice)
btn_choice.pack(pady=10)

frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Текст")

text_area = tk.Text(frame3, width=50, height=15)
text_area.pack(padx=10, pady=10)

def load_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Загрузить текст", command=load_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()