


def fib(n):
    a, b = 0,1
    sum=a+b

    while a+b < n:
        a, b = b, a+b
        sum=sum+a+b

    return sum

number=int(input('Please introduce a n: '))
sumnth_term= fib(number)
print('The sum of the n-th term of the fibonacci serie is: ', sumnth_term)
