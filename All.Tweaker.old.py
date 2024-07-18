import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tabs_data import tabs
import subprocess
import os

# Создаем основное окно
root = tb.Window(themename='vapor')
root.title('All Tweaker Beta')
root.attributes('-fullscreen', True)

# Переменные для хранения текущего шрифта и темы
current_font = ('Ubuntu Mono', 8)
current_theme = 'vapor'

# Функция для обновления стиля элементов с учетом выбранного шрифта
def update_font_style():
    style = ttk.Style()
    style.configure('TLabel', font=current_font)
    style.configure('TButton', font=current_font)
    style.configure('TCheckbutton', font=current_font)
    style.configure('TCombobox', font=current_font)
    style.configure('TTreeview', font=current_font)
    style.configure('TNotebook.Tab', font=current_font)

# Функция для обновления текущего шрифта
def update_font(event=None):
    global current_font
    font_family = font_family_var.get()
    font_size = font_size_var.get()
    current_font = (font_family, font_size)
    update_font_style()

# Функция для обновления текущей темы
def update_theme(event=None):
    global current_theme
    new_theme = theme_var.get()
    if new_theme != current_theme:
        root.style.theme_use(new_theme)
        current_theme = new_theme

# Создаем фрейм для размещения ползунка, выпадающих списков для шрифта и темы
font_and_theme_controls_frame = ttk.Frame(root)
font_and_theme_controls_frame.pack(side='bottom', anchor='se', padx=10, pady=(0, 10))

# Выпадающий список для выбора темы
theme_var = tk.StringVar(value=current_theme)
theme_values = root.style.theme_names()
theme_dropdown = ttk.Combobox(font_and_theme_controls_frame, textvariable=theme_var, values=theme_values)
theme_dropdown.pack(side='left', padx=(0, 5))
theme_dropdown.bind('<<ComboboxSelected>>', update_theme)

# Выпадающий список для выбора шрифта
font_family_var = tk.StringVar(value='Ubuntu Mono')
font_family_values = ['Roboto', 'Montserrat', 'Lato', 'Open Sans', 'Nunito', 'Arial', 'Times New Roman', 'Verdana', 'Georgia', 'Courier New', 'Ubuntu', 'Ubuntu Mono', 'Ubuntu Condensed', 'Ubuntu Light', 'Ubuntu Bold', 'System', 'Terminal']
font_family_dropdown = ttk.Combobox(font_and_theme_controls_frame, textvariable=font_family_var, values=font_family_values)
font_family_dropdown.pack(side='right', padx=(5, 0))
font_family_dropdown.bind('<<ComboboxSelected>>', update_font)

# Ползунок для выбора размера шрифта
font_size_var = tk.IntVar(value=10)
font_size_slider = ttk.Scale(font_and_theme_controls_frame, variable=font_size_var, from_=8, to=16, orient='horizontal')
font_size_slider.pack(side='right', padx=(0, 5))
font_size_slider.bind('<ButtonRelease-1>', update_font)

# Вызываем функцию для установки начального стиля
update_font_style()

# Функция для запуска файла
def run_file(file_name):
    print(f"Выполняется: {file_name}")
    subprocess.call(f'tweaks\\"{file_name}"', shell=True)
    # Здесь можно добавить логику для запуска скрипта или команды
    # subprocess.call(f'Utils\\PowerRun.exe ..\\tweaks\\"{file_name}"', shell=True)

# Кнопка "Выполнить"
execute_button = ttk.Button(root, text="Выполнить", command=lambda: run_file('Отключить UAC и smartscreen'))  # Пример, измените на нужное значение
execute_button.pack(side='top', padx=10, pady=10, fill='x')

# Поле для ввода сверху с отступом
search_entry_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_entry_var)
search_entry.pack(side='top', padx=10, pady=10, fill='x')

# Создание вкладок
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both', padx=10, pady=10)

# Создаем вкладки, подвкладки и подподвкладки
for tab_name, sub_tabs in tabs.items():
    tab_frame = ttk.Frame(tab_control)
    tab_control.add(tab_frame, text=tab_name)

    # Creamos canvas y scrollbar para la pestaña
    canvas = tk.Canvas(tab_frame, width=800, height=600)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = ttk.Scrollbar(tab_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Creamos el frame interno dentro del canvas
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    # Creamos las subvistas dentro del frame interno
    sub_tab_control = ttk.Notebook(inner_frame)
    sub_tab_control.pack(expand=1, fill='both', padx=10, pady=10)

    for sub_tab_name, elements in sub_tabs.items():
        if isinstance(elements, dict):  # Si el elemento es un diccionario, es una subvista
            sub_sub_tab_control = ttk.Notebook(sub_tab_control)
            sub_tab_control.add(sub_sub_tab_control, text=sub_tab_name)

            for sub_sub_tab_name, sub_elements in elements.items():
                sub_sub_tab_frame = ttk.Frame(sub_sub_tab_control)
                sub_sub_tab_control.add(sub_sub_tab_frame, text=sub_sub_tab_name)

                # Creamos dos columnas para los checkboxes
                left_column_frame = ttk.Frame(sub_sub_tab_frame)
                left_column_frame.pack(side='left', anchor='n', padx=10, pady=5)

                right_column_frame = ttk.Frame(sub_sub_tab_frame)
                right_column_frame.pack(side='left', anchor='n', padx=10, pady=5)

                for i, element in enumerate(sub_elements):
                    checkbox_var = tk.BooleanVar()
                    checkbox = ttk.Checkbutton(left_column_frame if i % 2 == 0 else right_column_frame,
                                              text=element, variable=checkbox_var,
                                              command=lambda file_name=element: run_file(file_name))
                    checkbox.pack(side='top', anchor='w', padx=5, pady=5)
        else:
            sub_tab_frame = ttk.Frame(sub_tab_control)
            sub_tab_control.add(sub_tab_frame, text=sub_tab_name)

            # Creamos dos columnas para los checkboxes
            left_column_frame = ttk.Frame(sub_tab_frame)
            left_column_frame.pack(side='left', anchor='n', padx=10, pady=5)

            right_column_frame = ttk.Frame(sub_tab_frame)
            right_column_frame.pack(side='left', anchor='n', padx=10, pady=5)

            for i, element in enumerate(elements):
                checkbox_var = tk.BooleanVar() 
                checkbox = ttk.Checkbutton(left_column_frame if i % 2 == 0 else right_column_frame,
                                          text=element, variable=checkbox_var,
                                          command=lambda file_name=element: run_file(file_name))
                checkbox.pack(side='top', anchor='w', padx=5, pady=5)

    # Actualizamos el tamaño del canvas
    inner_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Función para desplazar el canvas
    def scroll_canvas(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    # Vinculamos la función de desplazamiento al evento de desplazamiento del mouse
    canvas.bind_all("<MouseWheel>", scroll_canvas)

root.mainloop()

