def fib(n):
    golden = (1 + 5 ** 0.5) / 2
    print(golden)
    x=golden**n
    b=(1-golden)**n
    x1=x-b
    print(x1)
    x1=x1/(5**(1/2))
    print(5**(1/2))
    return x1

number=int(input('Please introduce a n: '))
nth_term= fib(number)
print('The n-th term of the fibonacci serie is: ', nth_term)
