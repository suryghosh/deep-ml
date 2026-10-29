def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    fib_series = []
    if n==0:
        return fib_series
    if n==1:
        fib_series=[0]
        return fib_series
    fib_series = [0,1]
    for i in range(2,n):
        present_val = fib_series[i-1]+fib_series[i-2]
        fib_series.append(present_val)
    return fib_series
    pass