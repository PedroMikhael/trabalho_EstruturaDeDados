import sys

# Aumenta o limite de recursão 
sys.setrecursionlimit(2000)

ALL_TEST_LISTS = [
    [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
    [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
    [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
    [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
    [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
    [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
    [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
    [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
    [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
    [50, 66, 32, 22, 54, 79, 21, 1, 80, 46]
]


def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps

def shell_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                comparisons += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
        gap //= 2
    return comparisons, swaps

def merge_sort_wrapper(arr):
    stats = {'comparisons': 0, 'swaps': 0}
    
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort(L)
            merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                stats['comparisons'] += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    stats['swaps'] += 1
                    i += 1
                else:
                    arr[k] = R[j]
                    stats['swaps'] += 1
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                stats['swaps'] += 1
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                stats['swaps'] += 1
                j += 1
                k += 1
    
    merge_sort(arr)
    return stats['comparisons'], stats['swaps']

def quick_sort_wrapper(arr):
    stats = {'comparisons': 0, 'swaps': 0}

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            stats['comparisons'] += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                stats['swaps'] += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        stats['swaps'] += 1
        return i + 1

    def quick_sort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort(array, low, pi - 1)
            quick_sort(array, pi + 1, high)

    quick_sort(arr, 0, len(arr) - 1)
    return stats['comparisons'], stats['swaps']

def heap_sort(arr):
    stats = {'comparisons': 0, 'swaps': 0}
    n = len(arr)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            stats['comparisons'] += 1
            if arr[l] > arr[largest]:
                largest = l

        if r < n:
            stats['comparisons'] += 1
            if arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            stats['swaps'] += 1
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        stats['swaps'] += 1
        heapify(arr, i, 0)
        
    return stats['comparisons'], stats['swaps']

def counting_sort(arr):
    # Swaps = total de atribuições/movimentações no array final
    
    if not arr: return 0, 0
    
    comparisons = 0
    moves = 0
    
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        moves += 1 
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        moves += 1
        
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        moves += 1
        
    for i in range(len(arr)):
        arr[i] = output[i]
        moves += 1
        
    return comparisons, moves


def run_all_tests():
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort_wrapper),
        ("Quick Sort", quick_sort_wrapper),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort)
    ]

    print(f"{'Algoritmo':<15} | {'Testes (C)':<10} | {'Trocas (T)':<10}")
    
    for i, lista_original in enumerate(ALL_TEST_LISTS):
        print("\n" + "="*45)
        print(f"LISTA {i+1}: {lista_original}")
        print("="*45)
        
        for name, func in algorithms:
            arr_copy = lista_original.copy()
            
            comp, swaps = func(arr_copy)
            
            assert arr_copy == sorted(lista_original), f"Erro no {name}"
            
            print(f"{name:<15} | {comp:<10} | {swaps:<10}")

if __name__ == "__main__":
    run_all_tests()