 
def v_iterative(n): # не рекурсия
    if n == 1 or n == 2:
        return 0
    if n == 3:
        return 1.5
    v = {1: 0, 2: 0, 3: 1.5}
    for i in range(4, n + 1):
        v[i] = ((i + 1) / (i**2 + 1)) * v[i - 1] - v[i - 2] - 2 * v[i - 3]
    return v[n]

print(v_iterative(4))  
print(v_iterative(5)) 
