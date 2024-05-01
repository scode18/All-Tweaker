import io
import os
import sys
import shutil
from contextlib import contextmanager

os.system('@echo off && title Install All Tweaker && mode con: cols=100 lines=25 && color a')

# Проверяем, существует ли каталог tweaks
if os.path.exists('tweaks'):
    print('Удаляем каталог tweaks')
    shutil.rmtree('tweaks')
else:
    print('Каталог tweaks не существует')

directory_path = '.'

# print('Все файлы в каталогах и подкаталогах')

# def get_all_paths(directory, paths=None):
#     if paths is None:
#         paths = []
#     for root, _, files in os.walk(directory):
#         for file in files:
#             path = os.path.join(root, file)
#             paths.append(path)
#     return paths

# # Example usage:
# all_paths = get_all_paths(directory_path)
# all_paths = [os.path.relpath(path) for path in all_paths]
# all_paths = [path for path in all_paths if not os.path.basename(path) == '.']
# print(all_paths)

print('Все имена каталогов и подкаталогов')

# Initialize an empty list to store the directory names
directory_names = []

# Use a for loop with os.walk() to iterate over all directories and subdirectories, excluding hidden directories
for root, dirs, files in os.walk(directory_path):
    # Append the name of the current directory to the list
    if not os.path.basename(root) == '.':
        directory_names.append(os.path.relpath(root))

# Print the list of directory names
print(directory_names)
directory_names = dirs

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

print('\nВсе имена каталогов (без подкаталогов)')

# Initialize an empty list to store the top-level directory names
directories = []

# Use a for loop with os.walk() to iterate over all directories and subdirectories, excluding hidden directories
for root, dirs, files in os.walk(directory_path):
    if root == directory_path:
        # Append the name of the current directory to the list
        directories.extend(dirs)
    else:
        # Break the loop to exclude subdirectories
        break

# Print the list of top-level directory names
print(directories)

# Папка, в которую будут копироваться файлы
destination_folder = 'tweaks'

# Создание папки назначения, если она не существует
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Перебираем каждый каталог и копируем файлы и подкаталоги в папку "tweaks"
# for directory in directories:
#     source_folder = os.path.join(os.getcwd(), directory)  # Путь к текущему каталогу
#     for root, dirs, files in os.walk(source_folder):
#         if directory == 'Кастомизация':
#             continue

#         for d in dirs:
#             src_dir = os.path.join(root, d)
#             dst_dir = os.path.join(destination_folder, os.path.relpath(src_dir, source_folder))
#             if not os.path.exists(dst_dir):
#                 os.makedirs(dst_dir)
#         for f in files:
#             src_file = os.path.join(root, f)
#             dst_file = os.path.join(destination_folder, os.path.relpath(src_file, source_folder))
#             shutil.copy(src_file, dst_file)
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
            subprocess.call(f'Utils\\\\PowerRun.exe tweaks\\\\"{checkbox_name}.reg"', shell=True)
            subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', f'tweaks\\\\{checkbox_name}.ps1'])

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
                        'Углубленная оптимизация + приватность Windows 11', 'Сделать копию реестра от Роджера Роуленда',    'Перезагрузка в Безопасный режим с поддержкой CMD', 'Терапия после обновлений винды',
                        'Хардкорная оптимизация + приватность Windows 10',  'Сделать копию реестра от studfile.net',        'Перезагрузка в Безопасный режим с поддержкой Сети','Обновить All Tweaker',
                        'Хардкорная оптимизация + приватность Windows 11',  'Импортировать копию реестра от studfile.net',  'Windows Vista - Server 2022 Activation',           'Выйти из All Tweaker',
    ],
'''

# Initialize an empty list to store the top-level directory names
top_directory_names = []

# Use a for loop with os.walk() to iterate over all directories and subdirectories, excluding hidden directories
for root, dirs, files in os.walk(directory_path):
    if root == directory_path:
        # Append the name of the current directory to the list
        top_directory_names.extend(dirs)
    else:
        # Break the loop to exclude subdirectories
        break

def get_all_paths(directory, extensions=None, exclude_files=None, exclude_dirs=None):
    if extensions is None:
        extensions = []
    if exclude_files is None:
        exclude_files = []
    if exclude_dirs is None:
        exclude_dirs = []
    paths = []
    for root, _, files in os.walk(directory):
        if root not in exclude_dirs:
            for file in files:
                path = os.path.join(root, file)
                if any(path.endswith(extension) for extension in extensions) and file not in exclude_files:
                    paths.append(path)
    return paths

extensions = ['.bat', '.cmd', '.ps1', '.exe', '.pow']
exclude_files = ['PowerRun.exe', 'pssuspend.exe', 'TI.exe']
exclude_dirs = ['База', 'tweaks', 'Source', 'Utils']

def print_list():
    with redirect_stdout(io.StringIO()) as print_to_string:
        for directory_name in top_directory_names:
            if directory_name not in exclude_dirs:
                directory_path = os.path.join(directory_name)
                if directory_name == 'Удалить приложения Microsoft':
                    exclude_subdirectories = ['Work']
                else:
                    exclude_subdirectories = []
                all_paths = get_all_paths(directory_path, extensions, exclude_files, exclude_dirs)
                all_paths = [os.path.relpath(path, directory_path) for path in all_paths]
                all_paths = [os.path.splitext(path)[0] for path in all_paths]
                all_paths = [path for path in all_paths if not os.path.basename(path) == '.' and not any(subdirectory in path for subdirectory in exclude_subdirectories)]
                # print(f'\nВсе файлы в каталоге {directory_name}')
                print('\n')
                print(f"'{directory_name.split('.')[-1]}':", end=' ')
                print(all_paths, end=',')

    result = print_to_string.getvalue() # получаем результат
    return result

result = print_list()
print(result)

# Рекурсивная функция для удаления reg файлов
# def delete_reg_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.reg'):
#                 file_path = os.path.join(root, file)
#                 os.remove(file_path)
#                 print(f"Удален файл: {file_path}")
def delete_reg_files(directory):
    exclude_dir = "Контекстное меню"
    for root, dirs, files in os.walk(directory):
        if root == directory:
            dirs[:] = [d for d in dirs if d != exclude_dir]
        for file in files:
            if file.endswith('.reg') or file == 'PowerRun.exe':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

delete_reg_files('tweaks')

with open('All.Tweaker.py', 'w', encoding='utf-8') as f:
    f.write(text + result + '''}
# New code to add label "All Tweaker..." to the tab "search_entry.placemh"
if 'Приватность' in tabs:
    tab_frame = ttk.Frame(tab_control)
    label = ttk.Label(tab_frame, text="""
    All Tweaker Beta by scode18 (Никита Соломон) — это утилита для тонкой настройки операционной системы и программного обеспечения, которая позволяет изменять определённые параметры для персонализации и оптимизации.
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
    elif tab_name == 'Исправление проблем':
        num_columns = 2
    elif tab_name == 'Кастомизация':
        num_columns = 3
    elif tab_name == 'Очистка':
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

os.system('python All.Tweaker.py')