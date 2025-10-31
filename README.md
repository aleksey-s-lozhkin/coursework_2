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

#### Абстрактный класс BaseCategory (`src/base_category`)
- **`class BeseCategory`** - Абстрактный класс для классов: Category, Order

#### Абстрактный класс BaseProduct (`src/base_product`)
- **`class BaseProduct`** - Абстрактный класс для классов: Product, Smartphone, LawnGrass

#### Класс ConsolMixin (`src/consol_mixin`)
- **`class ConsolMixin`** - Класс-миксин для вывода в консоль информации о том, от какого класса и с какими 
                            параметрами был создан объект

#### Класс ProductIterator (`src/product_iterator`)
- **`class ProductIterator`** - Вспомогательный класс, с помощью которого можно перебирать товары одной категории.

#### Класс Category (`src/category`)
- **`class Category`** - Класс для представления категории товаров в интернет-магазине.

#### Класс Product (`src/product`) 
- **`class Product`** - Класс для представления товара в интернет-магазине.

#### Класс Smartphone (`src/smartphone`) 
- **`class Smartphone`** - Класс для представления товара 'Smartphone' в интернет-магазине.

#### Класс LawnGrass (`src/lawn_grass`) 
- **`class LawnGrass`** - Класс для представления товара 'Lawn Grass' в интернет-магазине.

#### Утилиты (`src/utils`)
- **`read_json(path: str)`** - Функция для чтения json файла
- **`create_objects_from_json(data)`** - Функция для создания объектов из json файла

### Структура проекта

```
coursework_1/
├── src/
│   ├── base_category/
│   ├── base_product/
│   ├── consol_mixin/
│   ├── product_iterator/
│   ├── category/
│   ├── product/
│   ├── smartphone/
│   ├── lawn_grass/
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