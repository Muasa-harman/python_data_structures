## from collections import Counter
# a= "aaaaabbbbssss"
# my_counter = Counter(a)
# print(my_counter.most_common(2))

# # nametuple
# from collections import namedtuple
# Point = namedtuple('Point','a,b')
# pt = Point(1,-4)
# print(pt.a,pt.b)

# # OrderedDict
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['e'] = 5
# print(ordered_dict)

# # defaultdict
# from collections import defaultdict
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['c'])

# deque
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)


d.popleft()

# d.clear()
d.extendleft([4,5,6])
print(d)

d.rotate(1)
print(d)