import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція для інтегрування
def f(x):
    return x ** 2

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, samples=10000):
    x_random = np.random.uniform(a, b, samples)
    y_random = func(x_random)
    integral = np.mean(y_random) * (b - a)
    return integral

# Аналітичний метод для обчислення інтегралу
def analytical_integration(func, a, b):
    integral, _ = spi.quad(func, a, b)
    return integral

# Верхня і нижня межі інтегрування
a, b = 0, 2

# Обчислення інтегралу обома методами
monte_carlo_result = monte_carlo_integration(f, a, b)
analytical_result = analytical_integration(f, a, b)

# Виведення результатів
print(f"Інтеграл обчислений методом Монте-Карло: {monte_carlo_result}")
print(f"Інтеграл обчислений аналітично: {analytical_result}")

# Побудова графіку
x = np.linspace(-0.5, 2.5, 100)
y = f(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'r', label='f(x) = x^2')
plt.fill_between(x, y, where=[(i >= a and i <= b) for i in x], color='gray', alpha=0.5)
plt.title("Графік інтегрування f(x) = x^2 від 0 до 2")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axvline(x=a, color='k', linestyle='--', label='Межі інтегрування')
plt.axvline(x=b, color='k', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()