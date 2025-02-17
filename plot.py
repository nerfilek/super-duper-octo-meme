import time
import random
import numpy as np
import matplotlib.pyplot as graph  

# 1. Итеративный метод (самый быстрый для больших n)
def fibonacci_iterative(n):
    if n < 2:
        return [0] if n == 1 else [0, 1]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# 2. Рекурсивный метод (очень медленный)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 3. Мемоизация (ускорение рекурсивного метода)
def fibonacci_memoized(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# 4. Матричный метод (O(log n) - самый эффективный для огромных n)
def fibonacci_matrix(n):
    def multiply_matrices(A, B):
        return np.dot(A, B).astype(int)

    def matrix_power(matrix, exp):
        result = np.identity(len(matrix), dtype=int)
        while exp:
            if exp % 2:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            exp //= 2
        return result

    if n == 0:
        return 0
    base_matrix = np.array([[1, 1], [1, 0]], dtype=int)
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0, 0]

# 5. Генератор чисел Фибоначчи (для экономии памяти)
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Проверка, является ли число Фибоначчи (через математическое свойство)
def is_fibonacci_number(n):
    x1 = 5 * (n ** 2) + 4
    x2 = 5 * (n ** 2) - 4
    return int(x1 ** 0.5) ** 2 == x1 or int(x2 ** 0.5) ** 2 == x2

# Поиск ближайшего числа Фибоначчи
def closest_fibonacci(n):
    if n < 0:
        return 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a if (n - a) < (b - n) else b

# Генерация случайного числа Фибоначчи
def fibonacci_random(n):
    sequence = fibonacci_iterative(n)
    return random.choice(sequence)

# Вычисление золотого сечения (отношение двух последних чисел Фибоначчи)
def golden_ratio(n):
    sequence = fibonacci_iterative(n)
    return sequence[-1] / sequence[-2] if len(sequence) > 1 else 1

# Представление числа через уникальные числа Фибоначчи (Zeckendorf’s theorem)
def fibonacci_sum_representation(n):
    sequence = fibonacci_iterative(50)[::-1]  # Генерируем и переворачиваем последовательность
    result = []
    for num in sequence:
        if num <= n:
            n -= num
            result.append(num)
        if n == 0:
            break
    return result

# Измерение времени выполнения разных алгоритмов
def measure_time(method, n):
    start = time.time()
    if method == "recursive":
        sequence = [fibonacci_recursive(i) for i in range(n)]
    elif method == "memoized":
        sequence = [fibonacci_memoized(i) for i in range(n)]
    elif method == "matrix":
        sequence = [fibonacci_matrix(i) for i in range(n)]
    else:
        sequence = fibonacci_iterative(n)
    return sequence, time.time() - start

# Построение графика роста чисел Фибоначчи
def plot_fibonacci_growth(n):
    sequence = fibonacci_iterative(n)
    ratios = [sequence[i+1] / sequence[i] for i in range(1, len(sequence) - 1)]

    graph.plot(ratios, marker='o', linestyle='-', color='green', markersize=6, label="Golden Ratio Approximation")
    graph.axhline(y=1.618, color='red', linestyle='--', label="Theoretical Golden Ratio (1.618)")
    graph.title('Golden Ratio Approximation in Fibonacci Sequence')
    graph.xlabel('Index')
    graph.ylabel('Ratio')
    graph.legend()
    graph.grid(True)
    graph.show()

# Главная функция
def main():
    n = 35  # Количество чисел Фибоначчи для тестов

    # Измерение времени работы разных методов
    iter_seq, iter_time = measure_time("iterative", n)
    memo_seq, memo_time = measure_time("memoized", n)
    matrix_seq, matrix_time = measure_time("matrix", n)

    # Рекурсия медленная, выполняем только для малых n
    if n <= 20:
        rec_seq, rec_time = measure_time("recursive", n)
    else:
        rec_seq, rec_time = [], float('inf')

    # Вывод результатов
    print("Iterative:", iter_seq, f"Time: {iter_time:.6f} sec")
    print("Memoized:", memo_seq, f"Time: {memo_time:.6f} sec")
    print("Matrix:", matrix_seq, f"Time: {matrix_time:.6f} sec")
    if rec_seq:
        print("Recursive:", rec_seq, f"Time: {rec_time:.6f} sec")

    # Проверка, является ли число Фибоначчи
    num_to_check = 55
    print(f"Is {num_to_check} a Fibonacci number?", is_fibonacci_number(num_to_check))

    # Ближайшее число Фибоначчи
    num = 72
    closest = closest_fibonacci(num)
    print(f"Closest Fibonacci number to {num}: {closest}")

    # Генерация случайного числа Фибоначчи
    random_fib = fibonacci_random(n)
    print(f"Random Fibonacci number: {random_fib}")

    # Вычисление золотого сечения
    phi = golden_ratio(n)
    print(f"Golden Ratio approximation: {phi}")

    # Разложение числа в сумму чисел Фибоначчи
    num_to_represent = 88
    representation = fibonacci_sum_representation(num_to_represent)
    print(f"Zeckendorf Representation of {num_to_represent}: {representation}")

    # График роста чисел Фибоначчи и золотого сечения
    plot_fibonacci_growth(n)

if __name__ == "__main__":
    main()