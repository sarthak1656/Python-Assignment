# See_boolean = (4 * 3 > 10) and (6 + 5 >= 11) //True
# print(See_boolean)

# print(1-0.9 == 0.1)  //False

# x=[1,2,3]                   
# y=[1,2,3]
# print(x == y)   //True
# print ( x is y) //False
# l1 = [23,24,25]
# l2 = [26,27,28]
# l3 = l1
# print("Return Value :  ", l1 > l2)  //Return Value :   False
# print("Return Value :  ", l1 !=l2)  //Return Value :   True
# print("Return Value :  ", l3 == l2) //Return Value :   False


# print(bool(2)) //True
# print(1-0.9==.1)//False

# import decimal 
# x=decimal.Decimal(3.14)
# y=decimal.Decimal(2.74) 
# print( x*y) //8.603600000000001010036498883


# decimal.getcontext().prec=4 
# print( x*y) //8.604


# import fractions 
# print( fractions.Fraction(3,4))  3/4
# print(fractions.Fraction(0.5))  1/2

# a={30,20,10} 		
# b={40,20,50}
# print( a.difference(b) )  //{10, 30}
# print( a.intersection(b) ) //{20}
# print( a is b ) //False


# s1={"ab",3,4,(5,6)}
# s2=("ab",7,(7,6))
# s1.add(s2)
# s1.add(frozenset(s2))
# print(s1)  //{3, 4, 'ab', frozenset({(7, 6), 7, 'ab'}), (5, 6), ('ab', 7, (7, 6))}


# list1 = [1,2,3, 4]
# print(list1*2)  //[1, 2, 3, 4, 1, 2, 3, 4]


# tpl=('a','b','c')
# x,y,z= tpl
# print(x,y,z)  // a b c
# tpl[1]= 'c' //TypeError: 'tuple' object does not support item assignment


# dictionary ={1:"beek", 2:"for", 3:"beeks"}
# print(del.dictionary)  // error


# test = {1:'A', 2:'B', 3:'C'}
# del test[1]
# test[1] = 'D'
# del test[2]
# print(len(test)) //2


# a=dict(zip('packt', range(5)))
# print(a,len(a),a['c'])  #{'p': 0, 'a': 1, 'c': 2, 'k': 3, 't': 4} 5 2
# print(a.keys(),a.values(),a.items()) #dict_keys(['p', 'a', 'c', 'k', 't']) dict_values([0, 1, 2, 3, 4]) dict_items([('p', 0), ('a', 1), ('c', 2), ('k', 3), ('t', 4)])
# a.update({'a':1})
# print(a) #{'p': 0, 'a': 1, 'c': 2, 'k': 3, 't': 4}
# a.update(a=22)
# print(a) #{'p': 0, 'a': 22, 'c': 2, 'k': 3, 't': 4}
# a.pop('a')
# print(a) #{'p': 0, 'c': 2, 'k': 3, 't': 4}



# x = ('key1', 'key2', 'key3')
# y = 0
# newd = dict.fromkeys(x, y)
# print(newd)  {'key1': 0, 'key2': 0, 'key3': 0}

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6} 
# # sorted(list(d))
# print(d)  #{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
# sorted(list(d),key=d.__getitem__)
# print(d)
# sorted(list(d),key=d.__getitem__,reverse=True)
# print(d)
# sorted(list(d.values()))
# print(d)



# dictionary1 = {'Google' : 1, 'Facebook' : 2, 'Microsoft' : 3 }
# dictionary2 = {'GFG' : 1,  'Microsoft' : 2, 'Youtube' : 3}
# dictionary1.update(dictionary2);
# for key, values in dictionary1.items():
#     print(key, values)

# Google 1
# Facebook 2
# Microsoft 2
# GFG 1
# Youtube 3




















