print('''
        # 5.2
        ''')
list_p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15, 16]
print(list_p[len(list_p)//2:])


print('''
        # 5.3
        ''')

del list_p[10:]
end = list_p[-3:]

list_p[-3:] = list_p[:3]
list_p[:3] = end
print(list_p)

print('''
        # 5.4
        ''')
def sort_for_two_key(item):
    return item[1]

list_p = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
list_p.sort(key=sort_for_two_key)
print(list_p)

print(len([[1, 2]]*3))

list_p = [1, 3, 14, 15, 1231, 123, 11, 10, 35, 5, 14]
if 14 in list_p and list_p.count(14) > 1: 
    for i in range(list_p.count(14)):
        list_p.remove(14)
print(list_p)

print('''
        # 5.4
        ''')
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import copy 
deep = copy.deepcopy(x)

print('''
        # 5.6
        ''')
x = (4, 2, 1, 5)
s = ((list(x)).sort())
print(s)
