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
1. Клонировать репозиторий
```bash
git clone git@github.com:normalisht/grossbit_test_task.git
```

2. Перейти в папку проекта
```bash
cd grossbit_test_task 
```

3. Создать виртуальную среду
```bash
python -m venv venv
```
Активировать виртуальную среду

Для Windows:
```bash
source venv/Scripts/activate
```

Для Linux:
```bash
source venv/bin/activate
```

4. Установить зависимости
```bash
pip install -r requirements.txt
```

5. На основе файла `.env.example` необходимо создать `.env` файл.
(Данные для POSTGRES необходимо указывать только при отключении режима 
дебага)

Для локальной проверки qr-кодов, необходимо указать в переменной SERVER_ADDR
локальный адрес своего ПК, и подключиться с телефона и ПК к одной сети.
Узнать локальный адрес ПК можно с помощью команды `ipconfig` на Windows и
`ifconfig` на Linux

#### В PDFKIT_PATH указать путь к файлу wkhtmltopdf

[Как установить wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

6. Перейти в папку приложения
```bash
cd app 
```

7. Выполнить миграции БД
```bash
python manage.py migrate
```

8. Заполнить БД
```bash
python manage.py load_data 
```
Данные берутся из файла `app/static/data/items.csv`
При необходимости можно добавить дополнительные товары.
#### Команда полностью очищает таблицу и удаляет все данные о товарах

9. Запустить проект
```bash
python manage.py runserver
```
