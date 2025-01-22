#Return uncommon elements of lists. Order of elements does not matter.
def find_uncommon_elements(my_list, my_list1):
  
    uncommon = set(my_list) ^ set(my_list1)  
    return list(uncommon)  

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

uncommon_elements = find_uncommon_elements(list1, list2)
print("Uncommon elements:", uncommon_elements)