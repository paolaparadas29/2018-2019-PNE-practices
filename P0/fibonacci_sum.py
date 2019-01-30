def fibonacci(n):
        sum=0
        number1 = 0
        number2 = 1  # 806515533049393
        i = 0
        while i < n:
            sum=sum+number1
            number2 = number1 + number2
            number1 = number2 - number1
            i += 1
        return sum

number=int(input('Please introduce a n: '))

if number<1:
    print('Please introduce a positive number')
else:
    sumnth_term= fibonacci(number)
    print('The sum of the n-th term of the fibonacci serie is: ', sumnth_term)
