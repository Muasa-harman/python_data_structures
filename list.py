mylist = ["mango", "strawbery","apple"]
print(mylist)

# mylist2 = [5,5,True, "yes i"]
# print(mylist2)

# item = mylist[-1]
# print(item)

# for i in mylist:
#     print(i)

#if condition
# if "mango" in mylist:
#     print("yes")

# else:
#     print("no")

#length of my list
# print(len(mylist))

#append list
mylist.append("banana")
print(mylist)

#insert in specific position
mylist.insert(1, "lemon")
print(mylist)

# #remove items
# item = mylist.pop()
# print(item)
# print(mylist)

# #remove specific item
# item = mylist.remove("apple")
# print(mylist)

# item = mylist.clear()
# print(mylist)

item = mylist.reverse()
print(mylist)

#slicing
mylist3 = [1,2,3,4,5,6,7,8,9]
a = mylist3[1:5]
print(a)

#step index
a = mylist[::2]
print(a)