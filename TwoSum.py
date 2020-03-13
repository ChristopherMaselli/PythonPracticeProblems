'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

hashMap = {}

target = 9

def AddToHashMap(array, target):
    global hashMap
    for i in range(len(array)):
        hashMap[(target - array[i])] = array[i]

def SearchMap(array, target):
    global hashMap
    for i in range(len(array)):
        if array[i] in hashMap:
            print(array[i], end=' ')
            print(hashMap[array[i]])


AddToHashMap(array, target)
SearchMap(array, target)