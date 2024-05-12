#Write a Python program that generates the Fibonacci series up to a specified number of terms.

def fibonacci(n):
    fib_series = []
  
    a, b = 0, 1
    # Generate Fibonacci sequence 
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Generate Fibonacci series
fib_series = fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:")
print(fib_series)
