''' lambda funciton let square of a number without a function'''

# square = lambda x : x*x
# print(square(6))



''' join() function '''

# a=("teri", "maaa","kaa","chud") #list tuple sequence kuch bhi ho skta hai
# final="-".join(a)
# print(final)



''' map function '''

# l=[1,2,3,4]
# square=lambda x : x*x
# square_list= map(square,l)
# print(list(square_list))



''' filter fucntion '''

# l=[1,2,3,4,5]

# def even(n):
#     if(n%2==0):
#         return True
#     return False

# onlyEven=filter(even,l)
# print(list(onlyEven))


''' reduce function and reduce in inside functools module '''

# from functools import reduce

# l=[1,2,3,4,5]
# sum= lambda a,b : a+b  #lambda function 
# print(reduce(sum,l))


''' write a programe list table of 7 and convert into string'''


# table=[str(7*i) for i in range(1,11)]

# s="\n".join(table)
# print(type(s))
# print(s)



''' filter a list which is divisible by 5 '''

# l=[10,3,5,8,40]
# def divisible(l):
#     if(l%5==0):
#         return True
#     return False
# ans=filter(divisible,l)
# print(list(ans))



''' write a program to find the max number in the list '''

# from functools import reduce

# l=[2,5,6,8,1,0]
# def max(a,b):
#     if(a>b):
#         return a
#     return b
    
# print(reduce(max,l))