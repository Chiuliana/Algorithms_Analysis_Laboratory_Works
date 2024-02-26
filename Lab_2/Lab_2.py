import time
import random
import matplotlib.pyplot as plt
import pandas as pd

# Implement sorting algorithms
def quick_sort(arr, left, right):
    if left < right:
        # Choose pivot using median-of-three strategy
        mid = (left + right) // 2
        if arr[mid] < arr[left]:
            arr[mid], arr[left] = arr[left], arr[mid]
        if arr[right] < arr[left]:
            arr[right], arr[left] = arr[left], arr[right]
        if arr[right] < arr[mid]:
            arr[right], arr[mid] = arr[mid], arr[right]

        pivot = arr[mid]

        # Partitioning
        i = left - 1
        j = right + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        # Recursively sort partitions
        quick_sort(arr, left, j)
        quick_sort(arr, j + 1, right)

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]  # from beginning to middle point
        right_arr = arr[len(arr) // 2:]  # from middle point to the end

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # leftmost element on left arr
        j = 0  # leftmost element on right arr
        k = 0  # index in the merged arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def heap_sort(arr):
    # Heapify subtree rooted at index i to satisfy heap property
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max-heap from input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract max element and maintain heap property
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # swap
            j -= 1

sorting_algorithms = {
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort,
    'Heap Sort': heap_sort,
    'Insertion Sort': insertion_sort
}
# Define input sizes
input_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
arr = [[random.randint(0, 1000000) for _ in range(length)] for length in input_sizes]

for i in arr:
    print(i)
timeQuick = []
for i in arr:
    N = len(i) - 1
    start = time.perf_counter()
    sorting_algorithms['Quick Sort'](i.copy(), 0, N)  # Access function using square brackets and key
    end = time.perf_counter()
    timeQuick.append(end - start)

timeMerge = []
for i in arr:
    start = time.perf_counter()
    sorting_algorithms['Merge Sort'](i.copy())
    end = time.perf_counter()
    timeMerge.append(end - start)

timeHeap = []
for i in arr:
    start = time.perf_counter()
    sorting_algorithms['Heap Sort'](i.copy())  # Corrected the function call
    end = time.perf_counter()
    timeHeap.append(end - start)

timeInsertion = []
for i in arr:
    start = time.perf_counter()
    sorting_algorithms['Insertion Sort'](i.copy())
    end = time.perf_counter()
    timeInsertion.append(end - start)

# Plotting the data
plt.plot(input_sizes, timeQuick, label='Quick Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Quick Sort Execution Time')
plt.legend()  # Adding legend
plt.show()

plt.plot(input_sizes, timeHeap, label='Heap Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Heap Sort Execution Time')
plt.legend()  # Adding legend
plt.show()

plt.plot(input_sizes, timeMerge, label='Merge Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Merge Sort Execution Time')
plt.legend()  # Adding legend
plt.show()

plt.plot(input_sizes, timeInsertion, label='Insertion Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Insertion Sort Execution Time')
plt.legend()  # Adding legend
plt.show()

# Display results in separate tables
headers = ["Input Size", 'Quick Sort', 'Heap Sort', 'Merge Sort', 'Insertion Sort']
df_quick = pd.DataFrame({'Input Size': input_sizes, 'Quick Sort': timeQuick})
df_merge = pd.DataFrame({'Input Size': input_sizes, 'Merge Sort': timeMerge})
df_heap = pd.DataFrame({'Input Size': input_sizes, 'Heap Sort': timeHeap})
df_insertion = pd.DataFrame({'Input Size': input_sizes, 'Insertion Sort': timeInsertion})

print("Quick Sort:")
print(df_quick)
print("\nMerge Sort:")
print(df_merge)
print("\nHeap Sort:")
print(df_heap)
print("\nInsertion Sort:")
print(df_insertion)

# Plotting the data
plt.plot(input_sizes, timeQuick, label='Quick Sort')
plt.plot(input_sizes, timeHeap, label='Heap Sort')
plt.plot(input_sizes, timeMerge, label='Merge Sort')
plt.plot(input_sizes, timeInsertion, label='Insertion Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithms Comparison')
plt.legend()  # Adding legend
plt.show()

data = []
for i in range(len(input_sizes)):
    n = input_sizes[i]
    data.append([n, timeQuick[i], timeHeap[i], timeMerge[i], timeInsertion[i]])

# Display results in a tables
headers = ["Input Size", 'Quick Sort', 'Heap Sort', 'Merge Sort', 'Insertion Sort']
df = pd.DataFrame(data, columns=headers)
print(df)


