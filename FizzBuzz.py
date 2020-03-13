'''
"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz”
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples
of both three and five print “FizzBuzz”."
'''


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def FizzBuzz(arr):
    for i in range(len(arr)):
        if a[i]%3 == 0 and a[i]%5 == 0:
            print("FizzBuzz")
        elif a[i]%3 == 0:
            print("Fizz")
        elif a[i]%5 == 0:
            print("Buzz")
        else:
            print("----")

FizzBuzz(a)
