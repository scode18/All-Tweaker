import os
import shutil

# Удаление .py файлов кроме самого себя, All.Tweaker.py и tabs.py
for file in os.listdir("."):
    if file.endswith(".py") and file not in ["All.Tweaker.py", "tabs.py", os.path.basename(__file__)]:
        os.remove(file)

# Удаление .bat файлов кроме All.Tweaker.Start.bat и update.bat
for file in os.listdir("."):
    if file.endswith(".bat") and file not in ["All.Tweaker.Start.bat", "update.bat"]:
        os.remove(file)

# Удаление файлов elevator.exe, launcher.exe и tweaks.7z если они существуют
for file in ["elevator.exe", "launcher.exe", "tweaks.7z"]:
    if os.path.exists(file):
        os.remove(file)

# Удаление файлов в папке Utils кроме 7za.exe busybox.exe elevator.exe launcher.exe PowerRun.exe
for file in os.listdir("Utils"):
    if file not in ["7za.exe", "busybox.exe", "elevator.exe", "launcher.exe", "PowerRun.exe"]:
        os.remove(os.path.join("Utils", file))

# Удаление папки goodbyedpi
if os.path.exists("goodbyedpi"):
    shutil.rmtree("goodbyedpi")

# Удаление ненужных папок в tweaks
for dir in os.listdir("tweaks"):
    path = os.path.join("tweaks", dir)
    if os.path.isdir(path) and dir not in ["База", "Исправление проблем", "Кастомизация", "Обновления", "Оптимизация MartyFiles", "Основная оптимизация", "Углубленная оптимизация", "Хардкор оптимизация", "Оптимизация YouTube", "Остальное", "Очистка", "Поддержка", "Приватность", "Программы", "Удалить приложения Microsoft", "Электропитание"]:
        shutil.rmtree(path)
    elif os.path.isfile(path) and dir not in ["База", "Исправление проблем", "Кастомизация", "Обновления", "Оптимизация MartyFiles", "Основная оптимизация", "Углубленная оптимизация", "Хардкор оптимизация", "Оптимизация YouTube", "Остальное", "Очистка", "Поддержка", "Приватность", "Программы", "Удалить приложения Microsoft", "Электропитание", "make.py", "tabs.py"]:
        os.remove(path)
        
# Удаление файлов "Терапия после обновления Windows" и "Отключить телеметрию Браузеров" из директории tweaks\База
base_dir = os.path.join("tweaks", "База")

files_to_delete = [
    "Терапия после обновления Windows",
    "Отключить телеметрию Браузеров"
]

for filename in files_to_delete:
    for ext in [".bat", ".cmd"]:
        file_path = os.path.join(base_dir, filename + ext)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Файл '{filename + ext}' успешно удален.")
        else:
            print(f"Файл '{filename + ext}' не найден.")

# Удаление ненужных папок в tweaks\Оптимизация
for dir in os.listdir("tweaks/Оптимизация"):
    if dir not in ["MartyFiles", "Основная оптимизация", "Углубленная оптимизация", "Хардкор"]:
        shutil.rmtree(os.path.join("tweaks/Оптимизация", dir))

# Удаление файлов в папке tweaks\Оптимизация YouTube
for file in os.listdir("tweaks/Оптимизация YouTube"):
    if file in ["Альт. версия (режим 5)/Автозапуск (удалить сервис).cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для Beeline (Corbina).cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для P.a.k.t LLC.cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для Park Telecom.cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для Sibirskie Seti.cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для МГТС.cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис) для Ростелеком (Онлайм).cmd", "Альт. версия (режим 5)/Автозапуск (установить сервис).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (Beeline) (Corbina).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (P.a.k.t LLC).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (Park Telecom).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (Sibirskie Seti).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (МГТС).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI (Ростелеком) (Онлайм).cmd", "Альт. версия (режим 5)/Запустить GoodbyeDPI.cmd", "Альт. версия (режим 6)/Автозапуск (удалить сервис).cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для Beeline (Corbina).cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для P.a.k.t LLC.cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для Park Telecom.cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для Sibirskie Seti.cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для МГТС.cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис) для Ростелеком (Онлайм).cmd", "Альт. версия (режим 6)/Автозапуск (установить сервис).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (Beeline) (Corbina).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (P.a.k.t LLC).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (Park Telecom).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (Sibirskie Seti).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (МГТС).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI (Ростелеком) (Онлайм).cmd", "Альт. версия (режим 6)/Запустить GoodbyeDPI.cmd"]:
        os.remove(os.path.join("tweaks/Оптимизация YouTube", file))

configs_dir = "Configs"
file_to_delete = "Конфиг All Tweaker от Хауди Хо.bat"

if os.path.exists(os.path.join(configs_dir, file_to_delete)):
    os.remove(os.path.join(configs_dir, file_to_delete))
    print(f"Файл '{file_to_delete}' успешно удален из папки '{configs_dir}'.")
else:
    print(f"Файл '{file_to_delete}' не найден в папке '{configs_dir}'.")

os.system("update.bat")