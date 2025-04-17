# tuple = {}
# tuple[(1,2,4)] = 8
# tuple[(4,2,1)] = 10
# tuple[(1,2)] = 12
# _sum = 0
# for k in tuple:
#     _sum += tuple[k]
# print(len(tuple) + _sum) 33

# tuple = (1, 2, 3)
# print(2 * tuple)
# (1, 2, 3, 1, 2, 3)

# tuple=("Check")*3
# print(tuple) 
# CheckCheckCheck


# mylist1 = [100,20,30,40] 
# mylist2 = [10,50,60,90]
# if mylist1[1] in mylist2:
#    print("elements are overlapping")
# else:
#    print("elements are not overlapping")
# elements are not overlapping


# x1 = {'data', 'structure'} 
# x2 = {'python', 'java', 'c', 'data'} 
# x3 = x1 | x2
# print(x3) #{'java', 'python', 'c', 'structure', 'data'}
# print(x1.union(x2)) #{'java', 'python', 'c', 'structure', 'data'}
# print(x1.intersection(x2)) #{'data'}
# print(x1 & x2) #{'data'}
# print(x1.symmetric_difference(x2)) #{'java', 'python', 'c', 'structure'}
# print(x1 ^ x2) #{'java', 'python', 'c', 'structure'}



# from collections import namedtuple
# Book = namedtuple ('Book', ['name', 'ISBN', 'quantity']) 
# Book1 = Book('Hands on Data Structures', '9781788995573', '50') 
# print('Using index ISBN:' + Book1[1]) 
# print('Using key ISBN:' + Book1.ISBN)
# op: Using index ISBN:9781788995573
# op: Using key ISBN:9781788995573



# from collections import deque 
# s = deque() 
# print(s) 
# my_queue = deque([1, 2, 'Name']) 
# print(my_queue)
# op: deque([])
# op: deque([1, 2, 'Name'])


# from collections import Counter
# inventory = Counter('hello') 
# print(inventory) 
# print(inventory['l']) 
# print(inventory['e']) 
# print(inventory['o'])
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
# 2
# 1
# 1
