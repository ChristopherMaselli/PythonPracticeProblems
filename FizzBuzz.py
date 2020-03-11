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
