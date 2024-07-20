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

text = '''tabs = {
    'База': [
                        'Основная оптимизация + приватность Windows 10',    'Вернуть все службы',                           'Отключить UAC и smartscreen',                      'Windows 10 ALL version activator',
                        'Основная оптимизация + приватность Windows 11',    'Сделать бэкап служб',                          'Обычная перезагрузка',                             'Windows 11 ALL version activator',
                        'Углубленная оптимизация + приватность Windows 10', 'Сделать бэкап как bat',                        'Обычная перезагрузка в Безопасный режим',          'Отключить телеметрию Браузеров',
                        'Углубленная оптимизация + приватность Windows 11', 'Сделать копию реестра от Роджера Роуленда',    'Перезагрузка в Безопасный режим с поддержкой CMD', 'Терапия после обновления Windows',
                        'Хардкорная оптимизация + приватность Windows 10',  'Сделать копию реестра от studfile.net',        'Перезагрузка в Безопасный режим с поддержкой Сети','Обновить All Tweaker',
                        'Хардкорная оптимизация + приватность Windows 11',  'Импортировать копию реестра от studfile.net',  'Windows Vista - Server 2022 Activation',           'Выйти из All Tweaker',
    ],'''

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

extensions = ['.bat', '.cmd', '.ps1', '.exe', '.pow', 'reg']
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
                # all_paths = [os.path.splitext(path)[0] for path in all_paths]
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

# delete_reg_files('tweaks')

with open('tabs.py', 'w', encoding='utf-8') as f:
    f.write(text + result + '}')

os.system('python All.Tweaker.py')