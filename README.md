## Что бы развернуть этот сервер на своем пк нужно:
* Скачать этот репозиторий себе в свободную директорию. (Пример для unix систем).
```
$ git clone https://github.com/aronovY/test_task.git
```
* Создать и запустить виртуальное окружение в директории:
```
$ python3 -m venv my-env-name
$ source my-env-name/bin/activate
```
* Установить зависимости:
```
$ pip3 install -r requirements.txt
```
* Перейти в директорию test_task/application и запустить фаил main.py.
```
$ python3 main.py
```
--------------------
### Тестовые данные запросов в Postman:
##### Для получения списка работников:
```
curl --location --request GET '127.0.0.1:8080/get'
```

##### Для получения списка работников с именем "Ирина":
```
curl --location --request POST '127.0.0.1:8080/post?name=%D0%98%D1%80%D0%B8%D0%BD%D0%B0'
```

##### Для получения списка работников с фамилией "Козловская":
```
curl --location --request POST '127.0.0.1:8080/post?surname=%D0%9A%D0%BE%D0%B7%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F'
```

##### Для получения списка работников с отчеством "Дмитриевич":
```
curl --location --request POST '127.0.0.1:8080/post?patronymics=%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B5%D0%B2%D0%B8%D1%87'
```

##### Для получения списка всех работников мужчин:
```
curl --location --request POST '127.0.0.1:8080/post?sex=male'
```

##### Для получения списка всех работников старше 35 лет
```
curl --location --request POST '127.0.0.1:8080/post?age=35'
```