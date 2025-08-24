# Taifia

[![license](https://img.shields.io/github/license/Scorpi-ON/Taifia)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/badge/python-3.12-blue)](https://python.org/)
[![release](https://img.shields.io/github/v/release/Scorpi-ON/Taifia?include_prereleases)](https://github.com/Scorpi-ON/Taifia/releases)
[![downloads](https://img.shields.io/github/downloads/Scorpi-ON/Taifia/total)](https://github.com/Scorpi-ON/Taifia/releases)
[![code size](https://img.shields.io/github/languages/code-size/Scorpi-ON/Taifia.svg)](https://github.com/Scorpi-ON/Taifia)

[![Ruff linter](https://github.com/Scorpi-ON/Taifia/actions/workflows/linter.yaml/badge.svg)](https://github.com/Scorpi-ON/Taifia/actions/workflows/linter.yaml)
[![MyPy type checker](https://github.com/Scorpi-ON/Taifia/actions/workflows/type-checker.yaml/badge.svg)](https://github.com/Scorpi-ON/Taifia/actions/workflows/type-checker.yaml)
[![CodeQL (Python, GH Actions)](https://github.com/Scorpi-ON/Taifia/actions/workflows/codeql.yaml/badge.svg)](https://github.com/Scorpi-ON/Taifia/actions/workflows/codeql.yaml)

Курсовой проект по теории алгоритмов и формальных языков, продуктом которого является эмулятор одно- и многоленточной машины Тьюринга.

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

- графический интерфейс
- основной функционал — проверка слова на соответствие языку МТ и построение графика временной сложности алгоритмов
  МТ
- поддержка алгоритмов для одно- и многоленточных МТ, переключение между ними
- интерфейс должен оставаться отзывчивым при запущенном процессе проверки слова или построения графика
  (многопоточность)
- должен быть предусмотрен вывод протокола МТ и его экспорт в файл
- должен быть предусмотрен экспорт графика временной сложности в файл

## Особенности реализации

- [x] собственный формат алгоритма МТ и его парсер
- [x] множество предустановленных алгоритмов в папке [src/algorithm](./src/algorithm) (частично с комментариями)
- [x] возможность включить режим разработки, при котором алгоритмы перезагружаются при каждом запуске (позволяет удобно
  отлаживать алгоритм
  при его создании)
- [x] продвинутые инструменты для управления пакетами и анализа качества кода
- [ ] покрытие юнит-тестами
- [ ] автоматическая компиляция в единый исполнимый файл

## Стек

- **Python ^3.12** — язык программирования
- **uv** — пакетный менеджер
- **PyQt6** — библиотека для создания графического интерфейса
- **pyqtgraph** — библиотека для построения графиков в PyQt
- **pytest** — фреймворк для тестирования
- **Ruff** — инструмент для форматирования и анализа кода
- **MyPy** — статический типизатор Python
- **Nuitka** — компилятор Python

## Установка и запуск

0. Клонируйте репозиторий и перейдите в его папку.
1. Установите пакетный менеджер uv одним из способов. Например, для Windows:

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Установите зависимости:

```shell
uv sync --frozen --no-dev
```

3. Теперь запускать проект можно командой:

```shell
uv run -m src
```

## Модификация

Чтобы модифицировать проект, необходимо установить все зависимости, включая необходимые только для разработки:

```shell
uv sync
pre-commit install
```

Запустить форматирование кода, его линтинг и статический анализ типов можно следующими командами соответственно:

```shell
ruff format
ruff check --fix
mypy .
```

Обновить py-файл интерфейса после модификации ui-файла в Qt Designer можно командой:

```shell
uv run python -m PyQt6.uic.pyuic -o src/ui/form.py -x src/ui/form.ui
```
