# grossbit_test_task

## Что реализовано

### POST: /cache_machine/

Принимает объект вида:
```json
{
  "items": [1, 2, 3]
}
```
Где `items` содержит список ID товаров.
ID товаров может повторяться в списке несколько раз,
это значит, что кол-во этого товара в чеке увеличится.

На основе полученных ID формируется чек покупки товаров.

Возвращает qr-код ведущий на сформированный чек.


### GET: /media/<str:filename>
Возвращает ранее сформированный чек.

## Инструкция по запуску

1) Клонировать репозиторий
```bash
git clone git@github.com:normalisht/grossbit_test_task.git
```

2) Перейти в папку проекта
```bash
cd grossbit_test_task 
```

3) ### В settings.py указать путь к файлу wkhtmltopdf.exe для переменной PDFKIT_CONFIG
[Как установить wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

4) Создать виртуальную среду
```bash
python -m venv venv
```
И активировать виртуальную среду

Для Windows:
```bash
sources venv/Scripts/activate
```

Для Linux:
```bash
sources venv/bin/activate
```

5) Установить зависимости
```bash
pip install -r requirements.txt
```

6) На основе файла `.env.example` необходимо создать `.env` файл.
(Данные для POSTGRES необходимо указывать только при отключении режима 
дебага)
Для локальной проверки qr-кодов, необходимо указать в переменной SERVER_ADDR
локальный адрес своего ПК, и подключиться с телефона и ПК к одной сети

7) Перейти в папку приложения
```bash
cd app 
```

8) Выполнить миграции БД
```bash
python manage.py migrate
```

9) Заполнить БД
```bash
python manage.py load_data 
```
Данные берутся из файла `app/static/data/items.csv`
При необходимости можно добавить дополнительные товары.
Команду можно выполнить только один раз,
для повторного применения необходимо очистить таблицу `main_item`

10) Запустить проект
```bash
python manage.py runserver
```
