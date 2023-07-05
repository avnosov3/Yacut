# [YaCut](http://bkru.pythonanywhere.com/)

<details><summary>Russian language</summary>  
  
[Сервис](http://bkru.pythonanywhere.com/) укорачивания ссылок

## Техно-стек
* python 3.7.9
* flask 2.0.2
* flask-sqlalchemy 2.5.1
* flask-migrate 3.1.0


1. Клонировать репозиторий
```
git clone git@github.com:avnosov3/Yacut.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd Yacut
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
</details>

<details><summary>English language</summary>  
  
Short link [service](http://bkru.pythonanywhere.com/)

## Stack
* python 3.7.9
* flask 2.0.2
* flask-sqlalchemy 2.5.1
* flask-migrate 3.1.0


1. Clone repository
```
git clone git@github.com:avnosov3/Yacut.git
```
2. Go to the project folder and create a virtual environment
```
cd Yacut
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Activate a virtual environment
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Install dependencies from requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Create and populate the .env file
```
FLASK_APP=yacut
FLASK_ENV=<development or production>
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<specify secret key>
```
6. Apply migrations
```
flask db upgrade
```
7. Start project
```
flask run
```

## Author
[Artem Nosov](https://github.com/avnosov3)
</details>
