# myset = set()

# # add method
# myset.add(1)
# myset.add(2)
# myset.add(3)

# remove method
# myset.remove(1)

# discard
# myset.discard(3)

# clear
# myset.clear()
# pop
# print(myset.pop())
# print(myset)

# for i in myset:
#     print(i)

# if 1 in myset:
#     print("yes")

# union && intersection
# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# # union combines 2 sets without duplication
# u = odds.union(evens) 
# print(u)

# # provides only the elements on both sets 
# i = odds.intersection(primes)
# print(i)

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

# different method

# diff = setA.difference(setB)
# print(diff)

# symmetric_difference method
# diff = setB.symmetric_difference(setA)
# print(diff)

# update
# setA.update(setB)
# print(setA)

# intersection update
# setA.intersection_update(setB)
# print(setA)

# difference update
# setA.difference_update(setB)
# print(setA)


# # subsets - all the elements in setA are also in setB
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}

# print(setA.issubset(setB))

# # superset - contains all the numbers or all the elements from the second set are in first set 
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}

# print(setA.issuperset(setB))

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA.issubset(setB))