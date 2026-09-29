
"""fint the factorial of number using function recursionn"""

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# n=int(input("enter the number :"))
# print(f"the factorial of number is={factorial(n)}")




# def fun(name,ending):
#     print("good day",name)
#     print(ending)

# fun("ankit","thankyou")



'''function to find the greatest of three numbers'''

# def greatest(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             print("number 1 is greatest amongst all")
#     elif(num2>num3): print("number 2 greatest amongst")
#     else: print("number 3 is greatest amongst all")

# num1=int(input("enter num1 :"))
# num2=int(input("enter num2 :"))
# num3=int(input("enter num3 :"))
# greatest(num1,num2,num3)



'''finding celsius from fahrenheit'''

# def celsius(f):
#     c=5*(f-32)/9
# f=int(input("entert fahrenheit temperature :"))
# print(f"the celsius is {celsius(f)}")



'''remove the specific value from the list '''

# def remove(l,word):
#     if(word in l):
#         l.remove(word)

# l=["ankit","aman","mummy"]
# print(l)
# word="ankit"
# remove(l,word)
# print(l)



'''remove word or strip some part of the word '''

# def remove(l,word):
#     n=[]
#     for i in l:
#         if i!=word:
#             n.append(i.strip(word))
#     return n

# l=["ankit","aman","an"]
# word="ankit"
# print(remove(l,word))




'''solution of the tower of honoi'''

def tower(n,s,h,d):
    if(n==0):
        return
    tower(n-1,s,d,h)
    print(f"{s} -> {d}")
    tower(n-1,h,s,d)

n=int(input("enter the number :"))
tower(n,"A","B","C" )