# Імпортуємо бібліотеку PuLP
from pulp import *

# Створення моделі лінійного програмування
model = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

# Визначення змінних рішення
x1 = LpVariable("Лимонад", 0, None, LpInteger)  # Кількість "Лимонаду", не може бути від'ємною
x2 = LpVariable("Фруктовий_сік", 0, None, LpInteger)  # Кількість "Фруктового соку", не може бути від'ємною

# Функція цілі: Максимізація загальної кількості продуктів
model += x1 + x2, "Загальна_кількість"

# Додавання обмежень
model += 2 * x1 + 1 * x2 <= 100, "Обмеження_води"
model += x1 <= 50, "Обмеження_цукру"
model += x1 <= 30, "Обмеження_лимонного_соку"
model += 2 * x2 <= 40, "Обмеження_фруктового_пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Статус:", LpStatus[model.status])
print("Оптимальна кількість 'Лимонаду':", x1.varValue)
print("Оптимальна кількість 'Фруктового соку':", x2.varValue)
print("Максимальна загальна кількість продуктів:", value(model.objective))