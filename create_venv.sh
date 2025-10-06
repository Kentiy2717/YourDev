#!/bin/bash

echo "=== Создание виртуального окружения ==="
py -3.12 -m venv venv
echo "=== Активация виртуального окружения ==="
source venv/Scripts/activate

echo "=== Обновление pip ==="
py -m pip install --upgrade pip

echo "=== Установка зависимостей из requirements.txt ==="
pip install -r requirements.txt

echo "=== Готово! Виртуальное окружение создано и настроено ==="
echo "=== Активация виртуального окружения ==="
source venv/Scripts/activate