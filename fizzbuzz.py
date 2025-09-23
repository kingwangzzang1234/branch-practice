for k in range(5, 20+1):
    if k % 15 == 0:
        print('fizzbuzz')
    elif k % 3 == 0:
        print('fizz')
    elif k % 5 == 0:
        print('buzz')
    else:
        print(k)
