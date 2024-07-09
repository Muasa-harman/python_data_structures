# from itertools import product
# a = [1,2]
# b = [3]
# prod = product(a,b ,repeat=2)
# print(list(prod))

# # permutations
# from itertools import permutations
# a = [1,2,3]
# b = [3]
# perm = permutations(a,2)
# print(list(perm))

# # combinations
# from itertools import combinations,combinations_with_replacement
# a = [1,2,3]
# comb = combinations(a,2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# # accumulate
# from itertools import accumulate
# import operator
# a = [1,2,3,4]
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))

# groupby
from itertools import groupby

def smaller_than_3(a):
    return a < 3
a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key,value in group_obj:
    print(key, list(value))