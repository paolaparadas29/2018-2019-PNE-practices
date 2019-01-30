def fibonacci(n):
    number1=0
    number2=1#806515533049393
    i=1
    while i<n:
        number2 = number1 + number2
        number1= number2-number1
        i+=1
    return number1

nth_term= fibonacci(75)
print('The n-th term of the fibonacci serie is: ', nth_term)

