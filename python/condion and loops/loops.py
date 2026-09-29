# l=[23,"ankit",78,48.4,False]
# for i in range(len(l)):
#     print(l[i])




# l=[23,"ankit",78,48.4,False]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i+=1




#continue statement

# i=1
# while(i<10):
#     if(i==5):
#         i+=1
#         continue
#     print(i)
#     i+=1
    



'''printing table of a number given by user using for loop'''

# n=int(input("enter the number :"))
# for i in range(1,11):
#     print(f"{n} * {i}= {n*i}")





# printing table of number given by user using while

# n=int(input("enter the number :"))
# i=1
# while(i<=10):
#     print(f"{n} X {i} = {n*i}")
#     i+=1






'''greeting all the people in list whose name starts with "s"'''

# l=[]
# while(1):
#     l.append(input("enter the name :"))
#     ch=input("if you want to enter more than type(Y/N) :")
#     if(ch=="N" or ch== "n"):
#         print("\nCongrates you list has been creating")
#         break
# print()
# print(l)

# for name in l:
#     if(name.startswith("S")):
#         print(f"HI {name}")




'''checking the given number is prime or not'''

# n=int(input("enter the number(natural number) :"))

# if(n==1):
#     print("not prime number")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if((n%i)==0):
#             print("not a prime number")
#             break
    
#     else:
#         print("prime number")






'''factorial of number given by user using while loop'''

# n=int(input("enter the number :"))
# fact=1
# while(n>0):
#     fact*=n
#     n-=1

# print(fact)




''' factorial of number given by user using for loop '''

# n=int(input("enter the number :"))
# fact=1
# for i in range(n,0,-1):
#     fact*=i

# print(fact)






'''pattern printing  *
                     **
                     ***
                     ****    '''

# n=int(input("enter the length :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()





'''patter printing      * 
                      * * *
                    * * * * *    '''

# n=int(input("enter the length :"))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")

#     for j in range(1,2*(i)):
#         print("*",end=" ")
#     print()




'''printing the pattern      * * * * * 
                             *       *
                             *       *
                             *       *
                             * * * * *   '''

# n=int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()




'''printing the patter   *
                         *
                     * * * * *
                         *
                         *          '''

# n=int(input("enter the number only odd numebr :"))
# x=int(n/2)+1
# y=int(n/2)+1
# print(x,y)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==x or j==y):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




