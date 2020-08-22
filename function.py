def create_phone_number(n):
    #your code here
    my_iter = iter(n)
    a='('
    for _ in range(0,3,1):
        try:
            a+=str(next(my_iter))
        except:
            'need more number'
    a+=') '
    for _ in range(0,3,1):
        try:
            a+=str(next(my_iter))
        except:
            'need more number'
    a+='-'
    for _ in range(0,4,1):
        try:
            a+=str(next(my_iter))
        except:
            'Too much number'
    return a
