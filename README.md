# Описание
Проект представляет из себя сайт по отслеживанию посетителей хранилища по их пропускам.
- На главной странице представлены посетители с активными пропусками
- При переходе по ссылке "Список пользователей в хранилище" отслежвиаем посетителей, которые до сих пор находятся в хранилище
- Фильтрация посещения хранилища клиентами по их имени
# Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`
# Настройка окружения
При реализации приложения были добавлены приватные данные,в нашем случае при работе в файле `project/settings.py`. В них попали:
- название базы данных;
- имя пользователя;
- пароль;
- секретный ключ приложения;
- настройка отладочного режима
Для этого создадим воспользуемся библиотекой [environs](https://pypi.org/project/environs/) - это более функциональная альтернатива `python-dotenv`,а также файл `.env` на одном уровне с `settings.py` и пропишем в нем необходимые данные для приватизации:
```
export NAME_DB=checkpoint
export USER_DB=guard
export PASSWORD_DB=osim5
export SECRET_KEY_FROM_PROJECT=REPLACE_ME
export DEBUG=True
```
В файле `settings.py` импортируем библиотеку `environs` и подгрузим наши переменные окружения:
```
import os
from environs import Env

env = Env()
env.read_env()
```
Настроим БД:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': env("NAME_DB"),
        'USER': env('USER_DB'),
        'PASSWORD': env('PASSWORD_DB'),
    }
}
```
Секретный ключ сайта и режим отладки:
```
SECRET_KEY = env('SECRET_KEY_FROM_PROJECT')
DEBUG = env.bool("DEBUG", False)
```
# Реализация
- Функции(методы) `get_duration()` `format_duration()` `is_visit_long()` реализованы в `models.py` в теле модели `Visit`
- В контроллерах `active_passcards_view.py` `passcard_info_view.py` `storage_information_view.py` реализована логика фильтрации на стороне БД
