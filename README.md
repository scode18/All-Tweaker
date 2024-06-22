# All-Tweaker
![GitHub Tag](https://img.shields.io/github/v/tag/scode18/All-Tweaker?style=for-the-badge&label=release)
![PyPI - Version](https://img.shields.io/pypi/v/ttkbootstrap?style=for-the-badge&label=ttkbootstrap)
![GitHub repo size](https://img.shields.io/github/repo-size/scode18/All-Tweaker?style=for-the-badge)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/scode18/All-Tweaker/total?style=for-the-badge)
<br>
All Tweaker — это утилита для тонкой настройки операционной системы и программного обеспечения, которая позволяет изменять определённые параметры для персонализации и оптимизации. В ней объединены все лучшие твики, которые я нашел, включая Win 10 Tweaker, Booster X и другие. All Tweaker позволяет настроить внешний вид графического интерфейса пользователя, а также оптимизировать производительность системы и приложений.
## Отзыв от Антона
> Это лучше чем Booster X
## Поддержать автора
[Boosty](https://boosty.to/scode18/donate)
## Скоро будет полностью переделанный твикер
![image](https://github.com/scode18/All-Tweaker/assets/98618381/7acccc40-8593-4a92-a4af-77626d8ae2ed)

## Установка
[All.Tweaker.Beta.exe](https://shre.su/0KO3)
```batch
REM Скачиваем последний релиз
REM Распаковываем архив с помощью 7zip
All.Tweaker.Beta.exe
REM Переходим в директорию с твикером
cd "All Tweaker Beta"
REM Установка All Tweaker
setup.bat
install.bat
```
## Редактирование твиков и вкладок
```batch
REM Скачай репозиторий или каталоги Utils и Source
REM Загружаем Python
Utils\busybox wget https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
REM Установка Python без графического интерфейса
python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

REM Распаковываем архив с помощью 7zip
cd Utils
7za x ..\Source\Tweaks.7z
copy ..\Source\make.py .
REM Добавляем или удаляем твики, каталоги и подкаталоги
REM Твики содержат расширения ".bat", ".cmd", ".ps1", ".exe", ".pow", а ".reg" файлы удаляются

REM Запускаем make.py
make.py
```
## Если хочешь изменить количество столбцов
```python
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
```
## Скрины
![Снимок экрана (21)](https://github.com/scode18/All-Tweaker/assets/98618381/6acc543a-b5d2-459b-a350-509c479dfcb3)
![photo_2024-04-22_17-48-56](https://github.com/scode18/All-Tweaker/assets/98618381/fa0c3fa8-993e-4c1c-bc8c-681d38417835)
## Лицензия
Разрешение настоящим предоставляется бесплатно любому лицу, получившему копию.
данного программного обеспечения и связанных с ним файлов документации («Программное обеспечение») для решения
в Программном обеспечении без ограничений, включая, помимо прочего, права
использовать, копировать, изменять, объединять, публиковать, распространять, сублицензировать и/или продавать
копий Программного обеспечения и разрешать лицам, которым Программное обеспечение
предоставлено для этого при соблюдении следующих условий:

Вышеупомянутое уведомление об авторских правах и настоящее уведомление о разрешении должны быть включены во все
копии или существенные части Программного обеспечения.

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ
ПОДРАЗУМЕВАЕМЫЕ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ, ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ,
ПРИГОДНОСТЬ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ И НЕНАРУШЕНИЕ ПРАВ. НИ В КОЕМ СЛУЧАЕ НЕ ДОЛЖНО
АВТОРЫ ИЛИ ОБЛАДАТЕЛИ АВТОРСКИХ ПРАВ НЕСУТ ОТВЕТСТВЕННОСТЬ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УБЫТКИ ИЛИ ДРУГИЕ
ОТВЕТСТВЕННОСТЬ ПО ДОГОВОРУ, ПРАВИЛАМ ИЛИ ДРУГИМ ОБРАЗУ, ВЫТЕКАЮЩАЯ ИЗ:
ВНЕ ИЛИ В СВЯЗИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ИЛИ ДРУГИМИ ДЕЛАМИ В
ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ.
