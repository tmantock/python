def fib(n):
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1

    if n <= 1:
        return n

    i = 2

    while i <= n:
        memo[i] = memo[i - 1] + memo[i - 2]
        i += 1
    return memo[n]

print fib(9)
