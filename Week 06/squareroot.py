# Weekly task 06

# Author: Rebecca Feeley

def newton_sqrt(n, x):
    n = float(input("Please enter a positive number: "))
    x = float(input("Estimate your answer to square root of n: "))
    while x == 1 or x == n:
        sqrt = (0.5(x + (n/x))),
        return (sqrt)
    
print (newton_sqrt(5, 3))


 
# root = 0.5*(X + (N / X)) where X is any guess which can be assumed to be N or 1. 
''' 
n = float(input('What number would you like to squareroot?'))
x = float(input('Estimate your answer'))
final = (0.5*(x+(n/x)))
print (final)
for i in range(0,10):
    final = (0.5*(final+(n/final)))
    print (final)''' 
