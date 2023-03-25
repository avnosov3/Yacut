### Описание проекта:

Сервис укорачивания ссылок

### Автор: [Артём Носов](https://github.com/avnosov3)

### Техно-стек:
* python 3.7.9
* flask 2.0.2

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:avnosov3/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

создать БД и провести миграции

```
flask db init
flask db migrate
flask db upgrade
```

запустить проект

```
flask run
```
