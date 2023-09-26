def radix_sort(arr):
    max_value = max (arr)
    exp = 1
    while max_value // exp > 0:
        count = [0] * 10
        output = [0] * len (arr)
        for num in arr:
            count [(num // exp) % 10] += 1 
        for i in range (1, 10):
            count [i] += count[i - 1]
        for i in range(len (arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output [ count [index] - 1] = arr[i]
            count[index] -= 1
        for i in range (len (arr)):
            arr[i] = output [i]
        exp *= 10
# 예제 실행
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(numbers)
print (numbers)