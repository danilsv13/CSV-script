Cкрипт для обработки CSV-файла, поддерживающий операции: 
- фильтрацию с операторами «больше», «меньше» и «равно»
- агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения

Примеры запуска:

# Показать весь файл
python main.py --file products.csv

# Фильтрация: рейтинг < 4.7
python main.py --file products.csv --where rating<4.7

# Агрегация: средний рейтинг
python main.py --file products.csv --aggregate rating=avg

# Фильтрация и агрегация: минимальный рейтинг бренда xiaomi
python main.py --file products.csv --where brand=xiaomi --aggregate rating=min
