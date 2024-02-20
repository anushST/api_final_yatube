### Описание:
api_final_yatube - это блог в котором люди могут делиться со своими эмоциями с друзьями.

### Как запустить проект (Windows, Bash Terminal):
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:anushST/api_final_yatube.git
```
```
cd api_final_yatube
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установать зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
cd api_final_yatube
```
```
python manage.py migrate
```
Запустить проект (останьтесь в директории где вы выполняли миграции):
```
python manage.py runserver
```
### Примеры:
**GET api/v1/posts/**  
  
Response (JSON):
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```
  
**POST api/v1/posts/**  
  
Request (JSON):
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Response (JSON, status_code = 201):
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

