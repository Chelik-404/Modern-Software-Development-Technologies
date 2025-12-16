#Бондаренков Ум-252
#Практика 12
#Вариант 6

import tkinter as tk
from tkinter import messagebox
import requests
import json

root = tk.Tk()
root.title("Бондаренков Ум-252")

label = tk.Label(root, text="Введите имя пользователя GitHub:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.insert(0, "firehol")
entry.pack(pady=5)

def get_repo_data():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Введите имя пользователя!")
        return
    
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()

            filtered_data = {
                'company': user_data.get('company'),
                'created_at': user_data.get('created_at'),
                'email': user_data.get('email'),
                'id': user_data.get('id'),
                'name': user_data.get('name'),
                'url': user_data.get('url')
            }

            with open("result_firehol.json", "w", encoding="utf-8") as f:
                json.dump(filtered_data, f, indent=4, ensure_ascii=False)
            
            messagebox.showinfo("Успех", "Данные сохранены в result_firehol.json")
        else:
            messagebox.showerror("Ошибка", f"Не удалось получить данные. Код: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(pady=10)

root.mainloop()