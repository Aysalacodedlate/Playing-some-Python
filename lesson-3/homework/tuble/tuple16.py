#Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
a = (12, 234, 534, 65, 7, 87, 67, 45, 355)
b = sorted(a)
if a==b:
    print("Tuple is sorted")
else:
    print("Tuple is not sorted")