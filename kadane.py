def kadane(arr:[int], debug=False):
    result = arr[0]
    max_sum = arr[0]
    for i in range(len(arr)):
        max_sum = max(arr[i], max_sum+arr[i])
        result = max(result, max_sum)
    return result

arr = [-2, -3, 4, -1, -2, 1, 5, -1]

print(kadane(arr))