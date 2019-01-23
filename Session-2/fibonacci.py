def fib(n):
    a, b = 0,1
    i=2
    while i<n:
        a, b = b, a+b
        i=i+1
    return b

number=int(input('Please introduce a n: '))
nth_term= fib(number)
print('The n-th term of the fibonacci serie is: ', nth_term)
