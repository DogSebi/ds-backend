# Репозиторий к семинару "Основы backend-разработки"

## Что нужно сделать перед семинаром?
#### Собрать проект на виртуалке
1. зайти на виртуалку и склонировать на нее склонировать этот репозиторий
2. выполнить команду `docker build -t ds-backend`
3. запустить сервис командой `./run.sh`
4. открыть в браузере страничку *http://<vm_ip>:8080* и проверить, что выводится слово *"Hello"* 

#### Настроить VS Code для удаленного редактирования
1. установить VS Code на свою машину
2. установить в VS Code расширение "Remote - SSH" - [инструкция](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) (раздел "Getting started")
3. открыть проект в VS Code через Remote SSH

#### Запуск приложения
1. Через curl: `curl -X POST http://84.252.130.126:8080/readManyNumbers -H "Content-Type: application/json" -d "{"id_0": "10022", "id_1": "9965"}"`. Curl не декодирует символы
2. Через файл с клиентом: `python3 src/plate_reader_client.py 10022 9965`. 10022, 9965 - id изображений