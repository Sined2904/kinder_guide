# kinder_guide

### Описание
Проект, где можно найти курсы, школу, детский сад или репетитора для своего ребенка


### Технологии
requests==2.26.0
Django==3.2
djangorestframework==3.12.4
djangorestframework-simplejwt==5.2.2
djoser==2.2.0
PyJWT==2.1.0
django-filter==22.1
Pillow==9.5.0
python-dotenv==0.19.2

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Заполните файл .env
- В корневой папке проекта выполните команду:
```
docker compose up 
```

### Описание переменных окружения
POSTGRES_DB - название БД
POSTGRES_USER - имя пользователя БД
POSTGRES_PASSWORD - пароль пользователя БД
DB_NAME - название БД
DB_HOST - адрес БД
DB_PORT - порт БД
SECRET_KEY - криптографическая подпись Django
DEBUG - статус режима дебаг


### Авторы
Нестеренко Никита
Сашкина Кристина
Соловьев Эдуард
Пиневич Денис
Сарафанова Татьяна

Github - Sined2904
Den2904@yandex.ru
TG - @PinevichD