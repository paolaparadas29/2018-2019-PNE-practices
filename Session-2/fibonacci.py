def fibonacci(n):
    number1=0
    number2=1#806515533049393
    i=1
    while i<n:
        i+=1

        number1, number2= number2, number1+number2




    return number1

number=int(input('Please introduce a n: '))
nth_term= fibonacci(number)
print('The n-th term of the fibonacci serie is: ', nth_term)
