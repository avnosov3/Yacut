# [YaCut](http://bkru.pythonanywhere.com/)

[Сервис](http://bkru.pythonanywhere.com/) укорачивания ссылок

## Техно-стек
* python 3.7.9
* flask 2.0.2
* flask-sqlalchemy 2.5.1
* flask-migrate 3.1.0


1. Клонировать репозиторий
```
git clone git@github.com:avnosov3/yacut.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd yacut
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Активировать виртуальное окружение
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Установить зависимости из файла requirements.txt:
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Создать и заполнить файл .env
```
FLASK_APP=yacut
FLASK_ENV=development(режим разработки) или production(боевой режим)
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<указать секретный ключ>
```
6. Провести миграции
```
flask db upgrade
```
7. Запустить проект
```
flask run
```

## Автор
[Артём Носов](https://github.com/avnosov3)
