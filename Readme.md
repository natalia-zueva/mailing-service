
## Сервис управления рассылками, администрирования и получения статистики.

### Запуск на Windows:


1. Создайте виртуальное окружение python3 -m venv venv
2. Активируйте виртуальное окружение venv\Scripts\activate
3. Установите зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt
4. Установите redis глобально себе на компьютер, используйте wsl, 
терминал Ubuntu:
* sudo apt-get update
* sudo apt-get install redis
5. После установки запустите сервер Redis с помощью:
* sudo service redis-server start
* redis-cli
6. Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample:

SECRET_KEY=

DATABASES_NAME=
DATABASES_USER=
DATABASES_PASSWORD=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

CACHE_ENABLED=
CACHES_LOCATION=

7. В командной строке Windows запускайте сервис:
python manage.py runserver


### Работа с проектом

1. Можете загрузить тестовые данные либо создать свои:
python manage.py loaddata data.json
python manage.py loaddata blog.json

2. Зарегистрируйтесь на проекте, cоздайте своих клиентов, сообщения и саму рассылку
После создание рассылки нужно вызвать команду в терминале 
python manage.py runapscheduler

3. Для входа как superuser используйте доступы из файла users/management/commands/ccsu.py


