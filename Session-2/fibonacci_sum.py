def fib(n):
    a, b = 0,1
    sum=0
    i=1
    while i < n:
        sum=sum+a
        a, b = b, a+b
        i+=1


    return sum

number=int(input('Please introduce a n: '))
sumnth_term= fib(number)
print('The sum of the n-th term of the fibonacci serie is: ', sumnth_term)
