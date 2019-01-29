def sumn(n):
    total=0
    for i in range(n):
        total=total+i+1

    return total

# Main program
#num=int(input('Please introduce n: '))
total_sum = sumn(4)
print('the total sum is {}'.format(total_sum))
