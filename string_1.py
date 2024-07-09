# my_string = "I\'m a programmer"
# char = my_string[-1]
# substring = my_string[1:5]
# print(substring)


# for i in my_string:
#     print(i)

# if 'a' in my_string:
#     print('yes')
# else:
#     print('no')    

my_string = 'yes,this,is,all,well'
my_list = my_string.split(",")
new_string = ' '.join(my_list)
print(new_string)