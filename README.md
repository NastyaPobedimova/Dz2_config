# Общее описание
### Задание
Разработать инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости. Сторонние программы или библиотеки для получения зависимостей использовать нельзя. Зависимости определяются для файла-пакета **языка Python (pip)**. Для описания графа зависимостей используется представление **PlantUML**. Визуализатор должен выводить результат на экран в виде графического изображения графа.
### Ключами командной строки задаются:
- Путь к программе для визуализации графов;
- Путь к анализируемому пакету;
- Путь к файлу с изображением графа зависимостей;
# Реализованные функции
### get_dependencies
Функция рекурсивно извлекает зависимости пакета из файла package.py. Для каждого пакета:

 - Извлекаются метаданные: название и версия
 - Формируется уникальный идентификатор пакета
 - Загружаются зависимости через удаленный репозиторий
 - Рекурсивно обходятся все транзитивные зависимости
### generate_plantuml_graph
Генерирует PlantUML код для визуализации графа зависимостей на основе полученного списка зависимостей. Создает связи между пакетами в нотации PlantUML.
### visualize_dependencies
Основная функция, которая:

 - Получает зависимости через get_dependencies
 - Генерирует PlantUML код
 - Создает PNG-изображение графа зависимостей
 - Открывает сгенерированное изображение
### show_graph
Кроссплатформенная функция открытия сгенерированного графа в системном приложении по умолчанию.
# Сборка и запуск проекта
1. Установить Java (необходима для работы PlantUML)
2. Скачать утилиту PlantUML (https://plantuml.com/ru/download)
3. Клонировать репозиторий
```
git clone https://https://github.com/NastyaPobedimova/Dz2_config
```
4. Прейти в директорию репозитория
```
cd Dz2_config
```
5. Запустить dependency_visualizer.py с указанием всех необходимых ключей
```
py main.py plantuml-1.2024.8.jar package.py dependencery_graph.png
```
# Результат рыботы программы

![](https://github.com/NastyaPobedimova/Dz2_config/blob/main/dependencery_graph.png)

# Особенности реализации

 - Самостоятельная загрузка зависимостей
 - Рекурсивный обход транзитивных зависимостей
 - Визуализация с помощью PlantUML
 - Кроссплатформенное открытие графа
 - Обработка ошибок при загрузке и визуализации
# Технические требования

 - Python 3.7+
 - Java
 - Доступ к интернету
 - Установленная библиотека PlantUML
# Общие тесты

![](https://github.com/NastyaPobedimova/Dz2_config/blob/main/Test_screen.png)
