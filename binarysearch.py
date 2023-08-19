
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def power(a, b):
    return a ** b

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def main():
    test_list = [1, 2, 3, 5, 8]
    print("Binary Search Results:")
    print(binary_search(test_list, 6))  
    print(binary_search(test_list, 5))  

    print("\nPower Calculation:")
    print(power(3, 4))  # 81

    sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

    print("\nBubble Sort Results:")
    bubble_sort_sample = sample_data.copy()
    bubble_sort(bubble_sort_sample)
    print(bubble_sort_sample)

    print("\nMerge Sort Results:")
    merge_sort_sample = sample_data.copy()
    merge_sort_sample = merge_sort(merge_sort_sample)
    print(merge_sort_sample)

    print("\nQuick Sort Results:")
    quick_sort_sample = sample_data.copy()
    quick_sort_sample = quick_sort(quick_sort_sample)
    print(quick_sort_sample)

if __name__ == "__main__":
    main()
