#!/usr/bin/python3
#demonstration on append
list=[1,2,3,4,5]
list.append(6)
print(list)
#demonstration on remove
list.remove(5)
print(list)
#demonstration on pop
list.pop()
print(list)
#demonstration on sort
list.sort()
print (list)
#demonstration on reverse
list.reverse()
print (list)
#demonstration on extend
list_2 =[ 3,7,8,9 ]
list.extend(list_2)
print(list)

#demonstration on add()
set={1,3,4,5}
set.add(6)
print(set)
#demonstration on remove in set
list.remove(4)
print(list)
#demonstration on union
list5=list.union(list_2)
print(list5)
#demonstration on intersection
list3 =list.intersection(list_2)
print(list3)
#demonstration on difference
list4=list.difference(list_2)
print(list4)

#using list with union, intersection and difference
members=[1,2,3,4]
member1=[3,2,5,6,7,8]
print(members.union(member1))




