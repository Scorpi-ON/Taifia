# Taifia

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/badge/python-^3.12-blue)](https://python.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Простой эмулятор одно- и многоленточной машины Тьюринга

<details>
  <summary><h2>Скриншоты</h2></summary>
  <img src="https://github.com/user-attachments/assets/7929ffdd-2041-49fd-a10a-deb64c7371c1" width=30%>
  <img src="https://github.com/user-attachments/assets/b22d9a45-9be0-49dd-a93f-002382d749ca" width=30%>
  <br>
  <img src="https://github.com/user-attachments/assets/0f004a82-02ff-4b3f-9c55-b3da80a5559d" width=30%>
  <img src="https://github.com/user-attachments/assets/aabcb25b-e190-4dc4-a11a-994ce1c9e64f" width=30%>
  <br>
  <img src="https://github.com/user-attachments/assets/61c2aadc-9c80-41e6-8b67-799826a69f1e" width=30%>
</details>

## Основные требования

- [x] графический интерфейс
- [x] основной функционал — проверка слова на соответствие языку МТ и построение графика временной сложности алгоритмов
  МТ
- [x] поддержка алгоритмов для одно- и многоленточных МТ, переключение между ними
- [x] интерфейс должен оставаться отзывчивым при запущенном процессе проверки слова или построения графика
  (многопоточность)
- [x] должен быть предусмотрен вывод протокола МТ и его экспорт в файл
- [x] должен быть предусмотрен экспорт графика временной сложности в файл

## Особенности реализации

- [x] собственный формат алгоритма МТ и его парсер
- [x] множество предустановленных алгоритмов в папке [src/algorithm](./src/algorithm) (частично с комментариями)
- [x] возможность включить режим разработки, при котором алгоритмы перезагружаются при каждом запуске (позволяет удобно
  отлаживать алгоритм
  при его создании)
- [x] продвинутые инструменты для управления пакетами и анализа качества кода
- [ ] покрытие юнит-тестами

## Стек

- **[Python ^3.12](https://www.python.org/)** — язык программирования
- **[Poetry](https://python-poetry.org/)** — пакетный менеджер
- **[Ruff](https://astral.sh/ruff)** — инструмент для форматирования и анализа кода
- **[PyQt6](https://www.riverbankcomputing.com/software/pyqt/)** — библиотека для создания графического интерфейса
- **[pyqtgraph](https://www.pyqtgraph.org/)** — библиотека для построения графиков в PyQt
- **[pytest](https://docs.pytest.org/en/stable/)** — фреймворк для тестирования

## Установка и запуск

0. Клонируйте репозиторий и перейдите в его папку.
1. Установите [Poetry](https://python-poetry.org/).
2. Из папки проекта выполните установку зависимостей:

```shell
poetry install --without dev
```

3. Теперь запускать проект можно командой:

```shell
poetry run python -m src.main
```

## Модификация

Чтобы модифицировать проект, необходимо установить все зависимости, включая необходимые только для разработки:

```shell
poetry install
```

Обновить py-файл интерфейса после модификации ui-файла в Qt Designer можно командой:

```shell
poetry run python -m PyQt6.uic.pyuic -o src/ui/form.py -x src/ui/form.ui
```
