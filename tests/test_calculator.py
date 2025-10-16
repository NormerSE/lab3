# tests/test_calculator.py
import sys
import os
# Добавляем путь к src, чтобы импортировать calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(7, 0) == 0

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    # Проверяем, что функция вызывает исключение при делении на ноль
    try:
        calculator.divide(5, 0)
        assert False, "Expected ValueError"
    except ValueError:
        assert True