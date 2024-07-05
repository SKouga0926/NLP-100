def generate_numbers():
    for i in range(1, 11):
        yield i

numbers = generate_numbers()
# この時点では1から10までの数値はまだ生成されてない

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

def fibonacchi():
    a, b = 0, 1
    while True:
        yield a
        a = b
        b = a + b

fib = fibonacchi()

print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2
print(next(fib))  # 3