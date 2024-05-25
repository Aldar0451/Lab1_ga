 # Задание №1
def split_recursive(lst, n): # рекурсия
    if not lst:
        return [[] for _ in range(n)]
    smaller_split = split_recursive(lst[1:], n)
    smaller_split[lst[0] % n].append(lst[0])
    return smaller_split

print(split_recursive([1, 2, 3, 4, 5], 2))
print(split_recursive([1, 2, 3, 4, 5], 3)) 
