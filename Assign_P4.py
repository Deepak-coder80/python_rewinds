'''Develop a Python Program to find the single digit sum of a given
number
Examples:
Number = 123456789 = 45 = 9 ( single digit sum )
Number = 99999999992 = 11 = 2 ( single digit sum )
Number = 98989898 = 68 = 14 = 5 ( single digit sum)
'''
n = int(input("Enter the number"))

while n > 9:
    sum = int(0)
    while n > 0:
        r =int( n % 10)
        sum += r
        n = int(n/10)
    n = sum

print(sum)
