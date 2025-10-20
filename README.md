### Финансовая аналитика

Учебный проект на платформе SkyPro.

### Установка

#### Предварительные требования

- Python 3.8+
- Poetry (менеджер зависимостей)

### Установка Poetry

```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Linux/MacOS
curl -sSL https://install.python-poetry.org | python3 -
```

### Установка проекта

1. Клонируйте репозиторий:
```bash
git clone <https://github.com/aleksey-s-lozhkin/coursework_2/tree/feature/homework_14_1>
cd coursework_2
```

2. Установите зависимости через Poetry:
```bash
poetry install
```

3. Активируйте виртуальное окружение:
```bash
poetry shell
```

### Запуск

```bash
# Запуск демонстрации всех функций
poetry run python main.py

# Или с активированным окружением:
python main.py
```

После запуска отобразятся демонстрационные данные.

### Функциональность

#### Класс Category (`src/category`)
- **`class Category`** - Класс для представления категории товаров в интернет-магазине.

#### Класс Product (`src/product`) 
- **`class Product`** - Класс для представления товара в интернет-магазине.

#### Утилиты (`src/utils`)
- **`read_json(path: str)`** - Функция для чтения json файла
- **`create_objects_from_json(data)`** - Функция для создания объектов из json файла

### Структура проекта

```
coursework_1/
├── src/
│   ├── category/
│   ├── product/
│   └── utils/ 
├── data/
│   └── product.json
├── tests/  
├── main.py 
├── pyproject.toml
└── README.md
```

### Разработка

#### Добавление новых зависимостей
```bash
# Добавление production зависимости
poetry add package-name

# Добавление development зависимости
poetry add --group dev package-name
```

#### Запуск тестов
```bash
poetry run pytest
```

#### Форматирование кода
```bash
poetry run black .
poetry run isort .
```

### Демонстрация

Проект включает демонстрационный скрипт `main.py`

### Автор
aleksey.s.lozhkin@gmail.com

### Лицензия
Этот проект распространяется под лицензией MIT.