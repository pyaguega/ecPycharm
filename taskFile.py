# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def factorial(n):
    if n < 0:
        return 0
    elif n==1 or n == 0:
        return 1
    else:
        toReturn = 1
        while (n>1):
            toReturn *= n
            n -= 1
        return toReturn
print(factorial(5))
