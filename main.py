import requests
from requests.structures import CaseInsensitiveDict
from urllib.parse import urlparse
import json
import wget
import os

# Переменные программы
repo_link = str()
repo_segment = str()
branch = int()
branches_link = str()
branches_list = []
branch_link = str()

# Заголовки для запроса
headers = CaseInsensitiveDict()
headers['Authorization'] = 'Accept: application/vnd.github.v3+json'

def repo_name_split(link):
    '''
    Разбивает ссылку на элементы, и складывается в формате `'организация/репозиторий'`
    '''
    return '{0}/{1}'.format(
        urlparse(link).path.split('/', 3)[1], 
        urlparse(link).path.split('/', 3)[2])

def clear():
    '''
    Сбрасывает значения переменных (кроме `headers`)
    '''
    global repo_link, repo_segment, branch, branches_link, branches_list, branch_link

    repo_link = str()
    repo_segment = str()
    branch = int()
    branches_link = str()
    branches_list = []
    branch_link = str()

def set_branch():
    '''
    Выбор скачиваемой ветки
    '''
    global branch, branches_list
    print('Список веток репозитория: {0}'.format(branches_list))
    branch = int(input('Наберите цифру (не название) нужной ветки (отчёт начинается с нуля): '))
    if branch > len(branches_list) - 1:
        print('Неверная цифра!')
        set_branch()
    else:
        print('Вы выбрали ветку `{0}`'.format(branches_list[branch]))

def restart():
    '''
    При условии перезапускает программу
    '''
    print()
    _ = input('Перейти в начало программы? (Y/n): ')
    if _ == '' or _ == 'Y' or _ == 'y':
        start()
    else:
        os._exit(1)

def start():
    '''
    Запускает программу.

    Используются функции `clear`, `repo_name_split`, `set_branch` и `restart`.

    Происходит ввод ссылки на репозиторий, запрос названий его веток и скачивание
    выбранной ветки в архив возле исполняемого файла/python-скрипта.
    '''
    global repo_link, repo_segment, branch, branches_link, branches_list, branch_link
    clear()
    print('Команды: `e` -> выход из программы')
    repo_link = str(input('Введите ссылку на репозиторий GitHub: '))
    if repo_link != 'e':
        repo_segment = repo_name_split(repo_link)
        branches_link = 'https://api.github.com/repos/{0}/branches'.format(repo_segment)
        branches_response = requests.get(branches_link, headers=headers)
        branches = json.loads(branches_response.text)
        [branches_list.append(branch['name']) for branch in branches]
        set_branch()
        branch_link = 'https://api.github.com/repos/{0}/zipball/{1}'.format(repo_segment, branches_list[branch])
        file = wget.download(branch_link)
        restart()
    elif repo_link == 'e':
        os._exit(1)


if __name__ == '__main__':
    start()
