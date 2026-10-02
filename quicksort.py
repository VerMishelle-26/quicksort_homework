import time
import random
import matplotlib.pyplot as plt


# === К1: Фибоначчи + анализ стека вызовов ===
def fibonacci(n):
    """Рекурсивное n-е число Фибоначчи."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_with_trace(n, depth=0):
    """Фибоначчи с трассировкой стека вызовов."""
    indent = "  " * depth
    print(f"{indent}fibonacci({n})")
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_with_trace(n - 1, depth + 1) + fibonacci_with_trace(n - 2, depth + 1)


# === К2: Максимум через "разделяй и властвуй" ===
def find_max(arr, left=0, right=None):
    """Рекурсивный поиск максимума. Разделяй и властвуй."""
    if right is None:
        right = len(arr) - 1
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)
    return max(left_max, right_max)


# === К3: Быстрая сортировка ===
def quicksort(arr):
    """QuickSort. O(n log n) в среднем."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# === Сортировка вставками (для сравнения) ===
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# === Проверка ===
if __name__ == "__main__":
    print("=== К1: Фибоначчи ===")
    for n in range(8):
        print(f"fibonacci({n}) = {fibonacci(n)}")

    print("\n=== К1: Трассировка стека вызовов для n=5 ===")
    print(f"Результат: {fibonacci_with_trace(5)}")

    print("\n=== К2: Поиск максимума ===")
    test_arr = [3, 7, 2, 9, 1, 8, 5]
    print(f"Список: {test_arr}")
    print(f"Максимум: {find_max(test_arr)}")

    print("\n=== К3: QuickSort ===")
    arr = [64, 25, 12, 22, 11]
    print(f"Исходный: {arr}")
    print(f"Отсортированный: {quicksort(arr)}")

    # === К4: Сравнение скоростей ===
    print("\n=== К4: Сравнение QuickSort и сортировки вставками ===")
    sizes = [10, 100, 1000, 5000, 10000]
    quick_times = []
    insertion_times = []

    for size in sizes:
        arr = [random.randint(1, 100000) for _ in range(size)]

        start = time.perf_counter()
        quicksort(arr)
        quick_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        insertion_sort(arr)
        insertion_times.append(time.perf_counter() - start)

        print(f"Размер: {size:>6} | QuickSort: {quick_times[-1]:.6f} сек "
              f"| Вставками: {insertion_times[-1]:.6f} сек")

    # === График ===
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, quick_times, marker="o", label="QuickSort O(n log n)", color="blue")
    plt.plot(sizes, insertion_times, marker="s", label="Вставками O(n²)", color="red")
    plt.title("Сравнение QuickSort и сортировки вставками")
    plt.xlabel("Размер списка (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.legend()
    plt.grid(True)
    plt.savefig("quicksort_comparison_plot.png")
    print("\nГрафик сохранён: quicksort_comparison_plot.png")