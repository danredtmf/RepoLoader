# RepoLoader
Загрузка публичных репозиторий с GitHub.

## Оглавление
1. [Требования](#Требования)
2. [Подготовка](#Подготовка)

## Требования
- ![https://img.shields.io/badge/Python-3.10.0-blue](https://img.shields.io/badge/Python-3.10.0-blue) или выше
- Установленный пакет `requests` и `wget`, минимальные версии указаны в файле [requirements.txt](/requirements.txt)

## Подготовка
- Склонируйте репозиторий в любую папку на вашем компьютере.
- Рекомендуется создать виртуальное окружение внутри проекта через `pythonenv`
- Установите главные зависимости проекта:
    ```
    pip install requests wget
    ```
- Готово!

## Компиляция программы в .exe
Вам потребуется пакет `pyinstaller`:
```
pip install pyinstaller
```
- Компиляция в один файл:
    ```
    pyinstaller --onefile main.py
    ```
- Компиляция в каталог:
    ```
    pyinstaller --onedir main.py
    ```
