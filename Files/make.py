import io
import os
import sys
import shutil
from contextlib import contextmanager

dirs = [
    "Приватность",
    "Приватность\\Отключить телеметрию Браузеров",
    "Приватность\\Adamx",
    "Приватность\\BoosterX и ios1ph",
    "Приватность\\IT-спец. Денис Курец",
    "Приватность\\Optimizer",
    "Приватность\\Pulse",
    "Приватность\\Win 10 Tweaker",
    "Приватность\\windowser",
    "Оптимизация",
    "Оптимизация\\Оптимизация от ios1ph",
    "Оптимизация\\Оптимизация от ios1ph\\Основная оптимизация",
    "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация",
    "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация\\Режимы электропитания",
    "Оптимизация\\Оптимизация от ios1ph\\Хардкор",
    "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Адские режимы электропитания",
    "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Уменьшить количество svhost и другие твики",
    "Другая оптимизация",
    "Другая оптимизация\\Меньшая задержка ввода и более плавный игровой процесс",
    "Очистка",
    "Обновления Windows",
    "Удалить приложения Microsoft",
    "Исправление проблем",
    "Исправление проблем\\Отмена",
    "Исправление проблем\\Отмена\\Data Queue Size клава",
    "Исправление проблем\\Отмена\\Data Queue Size мышь",
    "Электропитание"
]

for dir in dirs:
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith((".bat", ".cmd")):
                filepath = os.path.join(root, file)
                with open(filepath, "rb") as f:
                    lines = f.readlines()
                with open(filepath, "wb") as f:
                    for line in lines:
                        if b"pause" not in line and b"exit" not in line:
                            f.write(line)

# Список с именами каталогов
directories = [
    "Приватность",
    "Оптимизация",
    "Другая оптимизация",
    "Очистка",
    "Обновления Windows",
    "Удалить приложения Microsoft",
    "Исправление проблем",
    "Электропитание"
]

# Папка, в которую будут копироваться файлы
destination_folder = 'tweaks'

# Создание папки назначения, если она не существует
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Перебираем каждый каталог и копируем файлы и подкаталоги в папку "tweaks"
for directory in directories:
    source_folder = os.path.join(os.getcwd(), directory)  # Путь к текущему каталогу
    for root, dirs, files in os.walk(source_folder):
        for d in dirs:
            src_dir = os.path.join(root, d)
            dst_dir = os.path.join(destination_folder, os.path.relpath(src_dir, source_folder))
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
        for f in files:
            src_file = os.path.join(root, f)
            dst_file = os.path.join(destination_folder, os.path.relpath(src_file, source_folder))
            shutil.copy(src_file, dst_file)

@contextmanager
def redirect_stdout(new_target):
    save_target, sys.stdout = sys.stdout, new_target # save current target and redirect to new target
    try:
        yield new_target
    finally:
        sys.stdout = save_target # restore the original target

def get_list(directory, directories=None):
    list_string = ""
    if directories is None:
        directories = [directory]
    files = []
    for d in directories:
        prefix = ""
        if d == "Приватность\\Отключить телеметрию Браузеров":
            prefix = "Отключить телеметрию Браузеров//"

        if d == "Приватность\\Adamx":
            prefix = "Adamx//"

        if d == "Приватность\\BoosterX и ios1ph":
            prefix = "BoosterX и ios1ph//"

        if d == "Приватность\\IT-спец. Денис Курец":
            prefix = "IT-спец. Денис Курец//"

        if d == "Приватность\\Optimizer":
            prefix = "Optimizer//"

        if d == "Приватность\\Pulse":
            prefix = "Pulse//"

        if d == "Приватность\\Win 10 Tweaker":
            prefix = "Win 10 Tweaker//"

        if d == "Приватность\\windowser":
            prefix = "windowser//"



        if d == "Оптимизация\\Оптимизация от ios1ph\\Основная оптимизация":
            prefix = "Основная оптимизация//"

        if d == "Оптимизация\\Оптимизация от ios1ph\\Основная оптимизация\\Режимы электропитания":
            prefix = "Основная оптимизация//Режимы электропитания"

        if d == "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация":
            prefix = "Углубленная оптимизация//"

        if d == "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация\\Режимы электропитания":
            prefix = "Углубленная оптимизация//Режимы электропитания//"

        if d == "Оптимизация\\Оптимизация от ios1ph\\Хардкор":
            prefix = "Хардкор//"

        if d == "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Адские режимы электропитания":
            prefix = "Хардкор//Адские режимы электропитания//"



        if d == "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Уменьшить количество svhost и другие твики":
            prefix = "Хардкор//Уменьшить количество svhost и другие твики//"
        if d == "Оптимизация\\Другая оптимизация\\Меньшая задержка ввода и более плавный игровой процесс":
            prefix = "Меньшая задержка ввода и более плавный игровой процесс//"



        if d == "Исправление проблем\\Отмена":
            prefix = "Отмена//"
        if d == "Исправление проблем\\Отмена\\Data Queue Size клава":
            prefix = "Data Queue Size клава//"
        if d == "Исправление проблем\\Отмена\\Data Queue Size мышь":
            prefix = "Data Queue Size мышь//"
        files += [prefix + os.path.splitext(f)[0] for f in os.listdir(d) if f.endswith((".bat", ".cmd", ".ps1", ".exe", ".pow")) and "PowerRun" not in f]
    print(files, end=',')

text = '''import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import ttkbootstrap as ttk
import subprocess

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

def execute():
    for checkbox_name, checkbox_var in checkboxes.items():
        if checkbox_var.get():
            subprocess.call(f'tweaks\\\\"{checkbox_name}"', shell=True)

def restart():
    subprocess.run(['shutdown', '/r', '/t', '0'])

# Кастомизация консоли
subprocess.call("title All Tweaker Beta & mode con: cols=100 lines=25 & color a & echo Welcome to All Tweaker", shell=True)

# Создание главного окна
root = ttk.Window(themename='vapor')
# root = ttk.Window(themename='cyborg')
# root.iconbitmap(r'icon.ico')
root.title('All Tweaker Beta')
root.attributes('-fullscreen', True)

# Создание вкладок
tab_control = ttk.Notebook(root)

tabs = {
    'База': [
                        'Основная оптимизация + приватность Windows 10',    'Вернуть все службы',                           'Отключить UAC и smartscreen',                      'Windows 10 ALL version activator',
                        'Основная оптимизация + приватность Windows 11',    'Сделать бэкап служб',                          'Обычная перезагрузка',                             'Windows 11 ALL version activator',
                        'Углубленная оптимизация + приватность Windows 10', 'Сделать бэкап как bat',                        'Обычная перезагрузка в Безопасный режим',          'Отключить телеметрию Браузеров',
                        'Углубленная оптимизация + приватность Windows 11', 'Сделать копию реестра от Роджера Роуленда',    'Перезагрузка в Безопасный режим с поддержкой CMD', 'Отключить телеметрию полностью',
                        'Хардкорная оптимизация + приватность Windows 10',  'Сделать копию реестра от studfile.net',        'Перезагрузка в Безопасный режим с поддержкой Сети','Терапия после обновлений винды',
                        'Хардкорная оптимизация + приватность Windows 11',  'Импортировать копию реестра от studfile.net',  'Windows Vista - Server 2022 Activation',           'Удалить все приложения Microsoft',
    ],
'''

# def print_list():
#     print("'Приватность':", end=' ')
#     get_list("Приватность", directories=["Приватность", "Приватность\\Отключить телеметрию Браузеров", "Приватность\\Adamx", "Приватность\\BoosterX и ios1ph", "Приватность\\IT-спец. Денис Курец", "Приватность\\Optimizer", "Приватность\\Pulse", "Приватность\\Win 10 Tweaker", "Приватность\\windowser"])

#     print("\n\n'Оптимизация':", end=' ')
#     get_list("Оптимизация", directories=["Оптимизация\\Оптимизация от ios1ph\\Основная оптимизация", "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация", "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация\\Режимы электропитания", "Оптимизация\\Оптимизация от ios1ph\\Хардкор", "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Адские режимы электропитания", "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Уменьшить количество svhost и другие твики"])

#     print("\n\n'Другая оптимизация':", end=' ')
#     get_list("Другая оптимизация", directories=["Оптимизация\\Другая оптимизация", "Оптимизация\\Другая оптимизация\\Меньшая задержка ввода и более плавный игровой процесс"])

#     print("\n\n'Очистка':", end=' ')
#     get_list("Очистка")

#     print("\n\n'Обновления Windows':", end=' ')
#     get_list("Обновления Windows")

#     print("\n\n'Удалить приложения Microsoft':", end=' ')
#     get_list("Удалить приложения Microsoft")

#     print("\n\n'Исправление проблем':", end=' ')
#     get_list("Исправление проблем", directories=["Исправление проблем", "Исправление проблем\\Отмена", "Исправление проблем\\Отмена\\Data Queue Size клава", "Исправление проблем\\Отмена\\Data Queue Size мышь"])

#     print("\n\n'Электропитание':", end=' ')
#     get_list("Электропитание")

def print_list():
    # сюда вставляете код функции print_list, заменив print на print_to_string
    with redirect_stdout(io.StringIO()) as print_to_string:
        print("'Приватность':", end=' ')
        get_list("Приватность", directories=["Приватность", "Приватность\\Отключить телеметрию Браузеров", "Приватность\\Adamx", "Приватность\\BoosterX и ios1ph", "Приватность\\IT-спец. Денис Курец", "Приватность\\Optimizer", "Приватность\\Pulse", "Приватность\\Win 10 Tweaker", "Приватность\\windowser"])

        print("\n\n'Оптимизация':", end=' ')
        get_list("Оптимизация", directories=["Оптимизация\\Оптимизация от ios1ph\\Основная оптимизация", "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация", "Оптимизация\\Оптимизация от ios1ph\\Углубленная оптимизация\\Режимы электропитания", "Оптимизация\\Оптимизация от ios1ph\\Хардкор", "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Адские режимы электропитания", "Оптимизация\\Оптимизация от ios1ph\\Хардкор\\Уменьшить количество svhost и другие твики"])

        print("\n\n'Другая оптимизация':", end=' ')
        get_list("Другая оптимизация", directories=["Оптимизация\\Другая оптимизация", "Оптимизация\\Другая оптимизация\\Меньшая задержка ввода и более плавный игровой процесс"])

        print("\n\n'Очистка':", end=' ')
        get_list("Очистка")

        print("\n\n'Обновления Windows':", end=' ')
        get_list("Обновления Windows")

        print("\n\n'Удалить приложения Microsoft':", end=' ')
        get_list("Удалить приложения Microsoft")

        print("\n\n'Исправление проблем':", end=' ')
        get_list("Исправление проблем", directories=["Исправление проблем", "Исправление проблем\\Отмена", "Исправление проблем\\Отмена\\Data Queue Size клава", "Исправление проблем\\Отмена\\Data Queue Size мышь"])

        print("\n\n'Электропитание':", end=' ')
        get_list("Электропитание")

    result = print_to_string.getvalue() # получаем результат
    return result

result = print_list()
# print(result)

with open('All Tweaker.py', 'w', encoding='utf-8') as f:
    f.write(text + result + '''}
# New code to add label "All Tweaker..." to the tab "search_entry.placemh"
if 'Приватность' in tabs:
    tab_frame = ttk.Frame(tab_control)
    label = ttk.Label(tab_frame, text="""
    All Tweaker Beta — это утилита для тонкой настройки операционной системы и программного обеспечения, которая позволяет изменять определённые параметры для персонализации и оптимизации.
    В ней объединены все лучшие твики, которые я нашел, включая Win 10 Tweaker, Booster X и другие.
    All Tweaker позволяет настроить внешний вид графического интерфейса пользователя, а также оптимизировать производительность системы и приложений.""")
    label.pack()
    tab_control.add(tab_frame, text='search_entry.placemh')

search_entry_var = StringVar()
search_entry = ttk.Entry(root, textvariable=search_entry_var)
search_entry.pack(side='bottom', padx=10, pady=10)
def select_all_for_tabs(tab_frame):
    select_all_checkbox_var = tk.BooleanVar()
    select_all_checkbox = ttk.Checkbutton(tab_frame, text='Выделить всё', variable=select_all_checkbox_var)
    select_all_checkbox.grid(row=0, column=0, sticky='w')

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

    if tab_name:
        select_all_for_tabs(tab_frame)

    num_columns = 1
    if tab_name == 'База':
        num_columns = 4
    elif tab_name == 'Приватность':
        num_columns = 3
    elif tab_name == 'Оптимизация':
        num_columns = 3
    elif tab_name == 'Другая оптимизация':
        num_columns = 2
    elif tab_name == 'Углубленная оптимизация и Хардкор':
        num_columns = 3
    elif tab_name == 'Исправление проблем':
        num_columns = 2
    elif tab_name == 'Удалить приложения Microsoft':
        num_columns = 2
    elif tab_name == 'Электропитание':
        num_columns = 3

    for i, checkbox_name in enumerate(checkbox_names):
        checkbox_var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(tab_frame, text=checkbox_name, variable=checkbox_var)
        checkbox.grid(row=i//num_columns+1, column=i%num_columns, sticky='w')
        checkboxes[checkbox_name] = checkbox_var

# Создание кнопок
execute_button = ttk.Button(root, text='Выполнить', command=execute)
restart_button = ttk.Button(root, text='Перезагрузка', command=restart)

# Размещение элементов
tab_control.pack(expand=1, fill='both')
# search_entry.pack(side='left', padx=10, pady=10)
search_entry.place(x=0, y=0)
# restart_button.pack(side='right', padx=10, pady=10)
# execute_button.pack(side='right', padx=10, pady=10)

# Create the "Выполнить" button
execute_button = ttk.Button(root, text='Выполнить', command=execute)

# Set the background color of the button
execute_button.configure(style='Custom.TButton')

# Create a custom style for the button
style = ttk.Style()
style.configure('Custom.TButton', background='black', foreground='white')

# Position the button in the top-right corner of the window
execute_button.place(relx=1.0, rely=0.0, anchor='ne')

# Запуск окна
root.mainloop()
''')

os.system('pip install ttkbootstrap')
os.system('python "All Tweaker.py"')
