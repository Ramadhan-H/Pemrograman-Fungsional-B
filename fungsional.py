#Nomor 1
data_list = [1,2,3]

def sum_sqr(x):
    return x * x

total = list(map(sum_sqr,data_list))
print(sum(total))


#Nomor 2

from functools import reduce
def tria(x):
    return reduce (lambda x,y: x*y, range(1,x+1))

print(tria(5))

#Nomor 3

number = [3]

def sqr(x):
    return x * x
total = list(map(sqr,number))
print(total)

#Nomor 4

kata =['rotator']

def is_plndr(x):
    if x == x [:: -1]:
        print(True)
    else:
        print(False)
    palindrome = list(filter(is_plndr,kata))
    print(palindrome)