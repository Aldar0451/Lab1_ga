 
def split_iterative(lst, n): # не рекурсия
    result = [[] for _ in range(n)]
    for i, value in enumerate(lst):
        result[i % n].append(value)
    return result

print(split_iterative([1, 2, 3, 4, 5], 2))  # [[1, 3, 5], [2, 4]]
print(split_iterative([1, 2, 3, 4, 5], 3))  # [[1, 4], [2, 5], [3]]
