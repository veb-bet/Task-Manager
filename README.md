# Task Manager API

Task Manager API — это простой **RESTful API** для управления задачами.  
Основан на **FastAPI**, **SQLAlchemy**, **Pydantic** и **SQLite**.  
Поддерживает создание, чтение, обновление и удаление (CRUD) задач.  

## Функции:
**Создание задач**  
**Просмотр списка задач**  
**Обновление задач**  
**Удаление задач**  
**Валидация данных с Pydantic**  
**Поддержка Docker**  
**Юнит-тесты с Pytest**  

---

## Технологии:
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Docker

---

## Установка и запуск

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```
### 2. Установите зависимости:
```bash
pip install -r requirements.txt
```
### 3. Запустите сервер:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

API будет доступно по адресу:
- http://127.0.0.1:8000/docs (Swagger UI)
- http://127.0.0.1:8000/redoc (ReDoc)

## Запуск в Docker
### 1. Соберите и запустите контейнер:
```bash
docker-compose up --build
```

Теперь API доступно на http://localhost:8000

---

## API-эндпоинты
| Метод   | Эндпоинт         | Описание               |
|---------|-----------------|------------------------|
| `POST`  | `/tasks/`       | Создать задачу        |
| `GET`   | `/tasks/`       | Получить список задач |
| `GET`   | `/tasks/{task_id}` | Получить задачу по ID |
| `PUT`   | `/tasks/{task_id}` | Обновить задачу       |
| `DELETE` | `/tasks/{task_id}` | Удалить задачу        |


Пример запроса POST /tasks/
```json
{
  "title": "Купить молоко",
  "description": "Не забыть купить молоко после работы"
}
```
Пример ответа:
```json
{
  "id": 1,
  "title": "Купить молоко",
  "description": "Не забыть купить молоко после работы",
  "completed": false
}
```

---

## Тестирование
Запуск тестов:

```bash
pytest tests/
```

