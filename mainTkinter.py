from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Создание поздравления")
root.geometry("500x700")


def click_button():
    index = praz_listbox.curselection()[0]
    P = praz[index]
    P = Spraz[P]

    name = entry.get()

    label = Label(text=("С " + P + ", " + name), font='Arial 18 bold', foreground=select())
    label.pack()

#праздники
praz_label = ttk.Label(text='Вкусы', font='Arial 18 bold')

Spraz = {'8 марта' : '8 марта', '23 февраля' : '23 февраля', '1 апреля' : '1 апреля', '9 мая' : '9 мая', 'годовщина': 'годовщиной', 'Новый год': 'Новым годом', 'День Рождения': 'Днем Рождения'}
praz = ['8 марта', '23 февраля', '1 апреля', '9 мая', 'годовщина', 'Новый год', 'День Рождения']
praz_var = Variable(value=praz)
praz_listbox = Listbox(listvariable=praz_var, font='Arial 16')
praz_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

#цвет
Scolors = {"красный" : "red", "зеленый" : "green", "синий" : "blue", "черный" : "black"}
position = {"padx": 6, "pady": 6, "anchor": NW}
colors = ["красный", "зеленый", "синий", "черный"]
selected_language = StringVar()  # по умолчанию ничего не выборанно

header = ttk.Label(text="Выберите цвет:")
header.pack(**position)

def select():
    color = selected_language.get()
    color = Scolors[color]
    return color

for lang in colors:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.pack(**position)


#имя
label = ttk.Label(text="Введите имя: ", font='Arial 16')
label.pack()

entry = ttk.Entry(width=100, font='Arial 16')
entry.pack(anchor=NW, padx=40, pady=6)


btn = ttk.Button(text="СОЗДАТЬ ПОЗДРАВЛНЕИЕ", command=click_button)
btn.pack()



root.mainloop()
