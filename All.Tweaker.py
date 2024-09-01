import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import ttkbootstrap as ttk
import os
import subprocess
import getpass
from datetime import datetime
import datetime

import sys
sys.path.insert(0, './tweaks')

from tabs import tabs

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}x{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def select_all_for_tabs(tab_frame):
    select_all_checkbox_var = tk.BooleanVar()
    select_all_checkbox = ttk.Checkbutton(tab_frame, text='Выделить всё', variable=select_all_checkbox_var)
    select_all_checkbox.grid(row=0, column=0, sticky='w')

    def select_all():
        select_state = select_all_checkbox_var.get()
        for checkbox in checkboxes.values():
            checkbox.set(select_state)

    select_all_checkbox.configure(command=select_all)

def execute_old():
    for checkbox_name, checkbox_var in checkboxes.items():
        if checkbox_var.get():
            tab_name = get_tab_name(checkbox_name)  # get the tab name from the checkbox name
            print(f'tweaks\\"{tab_name}\\{checkbox_name}"') 
            subprocess.call(f'tweaks\\"{tab_name}\\{checkbox_name}"', shell=True)
            # usage of JetBrains WinElevator (https://github.com/JetBrains/intellij-community/tree/master/native/WinElevator)
            # subprocess.run(['Utils\\launcher.exe', f'powershell.exe -ExecutionPolicy Bypass -File tweaks\\{checkbox_name}.ps1'])

def create_batch_file(activated_checkboxes):
    filename = f"Configs\\Config All Tweaker {datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.bat"
    # создаем папку Configs, если она не существует
    os.makedirs("Configs", exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write('chcp 65001\n')  # русская кодировка
        for checkbox_name, checkbox_var in checkboxes.items():
            if checkbox_var.get():
                tab_name = get_tab_name(checkbox_name)  # get the tab name from the checkbox name
                f.write(f'cmd /c "tweaks\\{tab_name}\\{checkbox_name}"\n')
    return filename

def update_config_file_list():
    global config_file_values
    config_file_values = [f for f in os.listdir('Configs') if f.endswith('.bat')]
    config_file_dropdown['values'] = config_file_values

def execute():
    activated_checkboxes = [checkbox_name for checkbox_name, checkbox_var in checkboxes.items() if checkbox_var.get()]
    if execute_function_var.get() == 'Создать конфиг':
        filename = create_batch_file(activated_checkboxes)
        subprocess.call(f'"{filename}"', shell=True)
        update_config_file_list()  # Обновляем список файлов конфигурации
    elif execute_function_var.get() == 'Выполнить':
        execute_old()

def get_tab_name(checkbox_name):
    for tab_name, checkbox_names in tabs.items():
        if checkbox_name in checkbox_names:
            return tab_name
    return None  # return None if the checkbox name is not found in any tab

def restart():
    subprocess.run(['shutdown', '/r', '/t', '0'])

# Кастомизация консоли
subprocess.call("title All Tweaker Beta & mode con: cols=100 lines=25 & color a & echo Welcome to All Tweaker", shell=True)

# Создаем основное окно
root = ttk.Window(themename='vapor')
root.title('All Tweaker Beta')
root.attributes('-fullscreen', True)

# Переменные для хранения текущего шрифта и темы
current_font = ('Ubuntu Mono', 8)
current_theme = 'Cyberpunk'

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

# Выпадающий список для выбора функции кнопки "Выполнить"
execute_function_var = tk.StringVar(value='Выполнить')
execute_function_values = ['Создать конфиг', 'Выполнить']
execute_function_dropdown = ttk.Combobox(font_and_theme_controls_frame, textvariable=execute_function_var, values=execute_function_values)
execute_function_dropdown.pack(side='left', padx=(0, 5))

# Выпадающий список для выбора файла конфигурации
config_file_var = tk.StringVar()
config_file_values = [f for f in os.listdir('Configs') if f.endswith('.bat')]
config_file_frame = ttk.Frame(font_and_theme_controls_frame)
config_file_dropdown = ttk.Combobox(config_file_frame, textvariable=config_file_var, values=config_file_values)
config_file_dropdown.pack(side='left', padx=(0, 5))

# Установка значения по умолчанию
default_config = 'Конфиг оптимизации от разработчика.bat'
if default_config in config_file_values:
    config_file_var.set(default_config)

def execute_config():
    selected_file = config_file_var.get()
    if selected_file:
        subprocess.call(f'Configs\\{selected_file}', shell=True)

execute_config_button = ttk.Button(config_file_frame, text='Выполнить конфиг', command=execute_config)
execute_config_button.pack(side='left', padx=(0, 5))

config_file_frame.pack(side='left', padx=(0, 5))

# Выпадающий список для выбора шрифта
font_family_var = tk.StringVar(value='GitHub: scode18')
font_family_values = ['Rust', 'Foxy', 'Frizon', 'Velocity', 'Roboto', 'Montserrat', 'Lato', 'Open Sans', 'Nunito', 'Arial', 'Times New Roman', 'Verdana', 'Georgia', 'Courier New', 'Ubuntu', 'Ubuntu Mono', 'Ubuntu Condensed', 'Ubuntu Light', 'Ubuntu Bold', 'System', 'Terminal', 'Small Fonts', 'Fixedsys', 'hooge 05_53', 'hooge 05_54', 'hooge 05_55']
font_family_dropdown = ttk.Combobox(font_and_theme_controls_frame, textvariable=font_family_var, values=font_family_values)
font_family_dropdown.pack(side='right', padx=(5, 0))
font_family_dropdown.bind('<<ComboboxSelected>>', update_font)

# Ползунок для выбора размера шрифта
font_size_var = tk.IntVar(value=10)
font_size_slider = ttk.Scale(font_and_theme_controls_frame, variable=font_size_var, from_=8, to=16, orient='horizontal')
font_size_slider.pack(side='right', padx=(0, 5))
font_size_slider.bind('<ButtonRelease-1>', update_font)

# Выпадающий список для выбора темы
theme_var = tk.StringVar(value=current_theme)
theme_values = root.style.theme_names()
theme_dropdown = ttk.Combobox(font_and_theme_controls_frame, textvariable=theme_var, values=theme_values)
theme_dropdown.pack(side='right', padx=(0, 5))

# Вызываем функцию для установки начального стиля
update_font_style()

# Создание кнопок
execute_button = ttk.Button(root, text='Выполнить', command=execute)
execute_button.pack(side='top', padx=10, pady=10, fill='x')

# Создание вкладок
tab_control = ttk.Notebook(root)

# New code to add label "All Tweaker..." to the tab "search_entry.placemh"
if 'Приватность' in tabs:
    tab_frame = ttk.Frame(tab_control)
    label = ttk.Label(tab_frame, text="""
    All Tweaker Beta (scode18) — это утилита для тонкой настройки операционной системы и программного обеспечения, которая позволяет изменять определённые параметры для персонализации и оптимизации.
    В ней объединены все лучшие твики, которые я нашел, включая Win 10 Tweaker, Booster X и другие.
    All Tweaker позволяет настроить внешний вид графического интерфейса пользователя, а также оптимизировать производительность системы и приложений.""")
    label.pack()
    username = getpass.getuser()  # get the current username
    tab_control.add(tab_frame, text=f'Привет, {username}')

search_entry_var = StringVar()
search_entry = ttk.Entry(root, textvariable=search_entry_var)
search_entry.pack(side='top', padx=10, pady=10, fill='x')

def select_all_for_tabs(tab_frame):
    select_all_checkbox_var = tk.BooleanVar()
    select_all_checkbox = ttk.Checkbutton(tab_frame, text='Выделить всё', variable=select_all_checkbox_var)
    # select_all_checkbox.grid(row=0, column=0, sticky='w')

    def select_all():
        select_state = select_all_checkbox_var.get()
        for checkbox in checkboxes.values():
            checkbox.set(select_state)

    def update_checkboxes(*args):
        entered_text = search_entry_var.get().lower()
        for checkbox_name, checkbox_var in checkboxes.items():
            if entered_text in checkbox_name.lower():
                checkbox_var.set(True)
            else:
                checkbox_var.set(False)

    select_all_checkbox.configure(command=select_all)
    search_entry_var.trace_add('write', update_checkboxes)

checkboxes = {}
for tab_name, checkbox_names in tabs.items():
    tab_frame = ttk.Frame(tab_control)
    tab_control.add(tab_frame, text=tab_name)

    canvas = tk.Canvas(tab_frame, width=800, height=600)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = ttk.Scrollbar(tab_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    if tab_name:
        select_all_for_tabs(inner_frame)

    num_columns = 2
    if tab_name == 'База':
        num_columns = 4
    elif tab_name == 'Обновления':
        num_columns = 1
    elif tab_name == 'Поддержка':
        num_columns = 1
    elif tab_name == 'Программы':
        num_columns = 3
    elif tab_name == 'Приватность':
        num_columns = 3

    for i, checkbox_name in enumerate(checkbox_names):
        checkbox_var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(inner_frame, text=checkbox_name, variable=checkbox_var)
        checkbox.grid(row=i//num_columns+1, column=i%num_columns, sticky='w')
        checkboxes[checkbox_name] = checkbox_var

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

canvas = tk.Canvas(tab_frame, width=800, height=600)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(tab_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Размещение элементов
tab_control.pack(expand=1, fill='both', padx=10, pady=10)

# Запуск окна
root.mainloop()
