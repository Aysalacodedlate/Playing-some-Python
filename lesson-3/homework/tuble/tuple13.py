#Find Second Smallest: From a given tuple, find the second smallest element.
numbers = (23, 34, 5, 24, 543, 34, 345, 345, 56, 324)
b = list(numbers)
print(b.reverse)
b = sorted (numbers, reverse = False)
print(b[1])

