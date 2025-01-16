import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string

# Функция генерации ключа
def generate_key():
    input_number = entry.get()
    
    # Валидация ввода: должно быть 6-значное число
    if not input_number.isdigit() or len(input_number) != 6:
        messagebox.showerror("Ошибка", "Пожалуйста, введите 6-значное число.")
        return
    
    # Разделение числа на части
    first_three = input_number[:3]
    last_three = input_number[3:]
    
    # Перестановка первых двух цифр в каждой части
    block1_num = first_three[1] + first_three[0] + first_three[2]
    block2_num = last_three[1] + last_three[0] + last_three[2]
    
    # Преобразование в целые числа для сложения
    try:
        num1 = int(block1_num)
        num2 = int(block2_num)
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный формат числа после перестановки.")
        return
    
    # Генерация случайных букв
    random_letters1 = ''.join(random.choices(string.ascii_uppercase, k=2))
    random_letters2 = ''.join(random.choices(string.ascii_uppercase, k=2))
    
    # Сумма чисел с ведущими нулями до 4 цифр
    key_sum = f"{num1 + num2:04d}"
    
    # Формирование ключа
    key = f"{block1_num}{random_letters1}-{block2_num}{random_letters2}-{key_sum}"
    
    # Отображение ключа
    key_var.set(key)

# Создание основного окна
root = tk.Tk()
root.title("Keygen Программа")
root.geometry("800x600")
root.resizable(False, False)

 
bg_image = Image.open("clash_of_clans.jpg")
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)   
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создание фрейма для содержимого
frame = tk.Frame(root, bg='#ffffff', bd=2)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Поле ввода (уменьшено в ширину)
label = tk.Label(frame, text="Введите 6-значное число:", font=("Arial", 12))
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12), width=6)  # Установлена ширина 6 символов
entry.grid(row=0, column=1, padx=10, pady=10)

# Кнопка генерации
generate_button = tk.Button(frame, text="Сгенерировать ключ", command=generate_key, font=("Arial", 12))
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Поле вывода ключа
key_var = tk.StringVar()
key_label = tk.Label(frame, textvariable=key_var, font=("Courier", 14), fg="blue")
key_label.grid(row=2, column=0, columnspan=2, pady=10)

# Запуск основного цикла
root.mainloop()
