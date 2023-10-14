import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]        # Put any number smaller than pivot to the left array
        right = [x for x in arr[1:] if x >= pivot]      # Put any number larger than or equal to pivot to the right array
        return quicksort(left) + [pivot] + quicksort(right)     # Recursive call with two smaller arrays

def generateRandomTestCase():
    length = random.randint(0, 20)  # Random array length between 0 and 20
    arr = [random.randint(-100, 100) for _ in range(length)]  # Random integer values between -100 and 100
    return arr

test_case = generateRandomTestCase()
print("Input array:", test_case)
sorted_array = quicksort(test_case)
print("Sorted array:", sorted_array)