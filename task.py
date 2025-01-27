def factorial_recursive(n):
    if n == 0 or n == 1:  # 0! 和 1! 都是 1
        return 1
    return n * factorial_recursive(n - 1)

n = 5
result = factorial_recursive(n)
print(f"{n} 的阶乘是: {result}")