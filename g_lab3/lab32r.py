 
def v_recursive(i, memo={1: 0, 2: 0, 3: 1.5}): # рекурсия
    if i in memo:
        return memo[i]
    memo[i] = ((i + 1) / (i**2 + 1)) * v_recursive(i - 1, memo) - v_recursive(i - 2, memo) - 2 * v_recursive(i - 3, memo)
    return memo[i]

print(v_recursive(4))  
print(v_recursive(5)) 
