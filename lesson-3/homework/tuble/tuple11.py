#Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.

a = ('du', 'se', 'chor', 'pay', 'jum', 'shan', 'pay', 'du', 'se', 'chor', 'pay', 'du', 'se')

#print(a.index('du', 8, 12))
#for du in range(a(0, 12)):
#    print(du)
#for du in range (0, 12):
#    print('du')
#wrong approaches allllllllllllllllllllll
#for du in enumerate(a):
#    print(du)

indices = [index for index, value in enumerate(a) if value == 'du']
print(indices)