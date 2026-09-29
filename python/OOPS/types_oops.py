
'''sinlge inheritance = derived class form base class'''

# class employee:
#     company="Itc"
#     def show(self):
#         print("the name of the company is {self.name} and salary is {self.salary}")

# class programmer(employee):
#     company="itc infotech"
#     def showlanguage(self):
#         print("the name is {self.name} and the is good with {self.language} language")

# a=employee()
# b=programmer()
# print(a.company,b.company,)





'''multiple inheritance = derived class form multiple base class '''

# class employee:
#     company="Itc"
#     name="ankit"
#     def show(self):
#         print(f"the name is  {self.name} and company name is {self.company}")

# class coder:
#     language="python"
#     def print(self):
#         print(f"your language is {self.language}")

# class programmer(employee,coder):
#     company="itc infotech"
#     def showlanguage(self):
#         print(f"the name is {self.name} and the is good with {self.language} language")

# a=employee()
# b=coder()
# c=programmer()

# a.show()
# b.print()
# c.showlanguage()




''' multilevel inheritance where base > derived > derived '''

# class employee:
#     a=1

# class programmer(employee):
#     b=2

# class manager(programmer):
#     c=3

# r=employee()
# print(r.a)
# t=programmer()
# print(t.a,t.b)
# y=manager()
# print(r.a,t.b,y.c)



''' mutilevel inheritance new example '''

# class employee:
#     god1="vishnu"

# class coder(employee):
#     god2="bholenath"

# class programmer(coder):
#     def show(self):
#         print(f"{self.god1} {self.god2} bramha dev sorry galat kaam chod diye hai")

# ans=programmer()
# ans.show()




''' super constructor use  is used to call parent auto matocally when derived class is called '''

# class employee:
#     def __init__(self):
#         print("jai shree ram")
#     a=1

# class programmer(employee):
#     def __init__(self):
#         super().__init__() 
#         print("jai shankar bhagwan")
#     b=2

# class manager(programmer):
#     def __init__(self):
#         super().__init__()
#         print("jai bramha dev")
#     c=3

# r=manager()
# print(r)


'''@classmethod use'''

# class employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"the value of attribute of class is {cls.a}")

# ans=employee()
# ans.a=45
# ans.show()



''' property decorator(@property) and setter(@name.setter) '''

# class employee:
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self,value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]

# ans=employee()
# ans.name="Ankit Prajapti"
# print(ans.fname,ans.lname)



''' operator overloading  add'''

# class number:
#     def __init__(self ,n):
#         self.n=n

#     def __add__(a,b):
#         return a.n + b.n

# n=number(1)
# m=number(2)

# print(n+m)


'''operator overloading use multiply '''

# class number:
#     def __init__(self,n):
#         self.n=n

#     def __mul__(self, other):
#         return self.n * other.n
    
# a=number(2)
# b=number(5)

# print(a*b)



''' assignment operator '''

# if (n:=len("ankit"))>3:
#     print("hello ankit")




''' match cases '''

# def check(n):
#     match n:
#         case 10:
#             return "less money"
#         case 50:
#             return "average money"
#         case 100:
#             return "very good"
#         case _:
#             return "not matched"
        
# n=int(input("enter the number :"))
# print(check(n))



''' merge and update the dictionary '''

# dict1={'a':1,'b':2}
# dict2={'b':1,'c':3}
# merge=dict1 | dict2
# print(merge)




''' exception hadling  '''

# try:
#     name=int(input("enter the name :"))
#     print(name)

# except ValueError:
#     print("teri maa ka chud")

# else:
#     print("program is finished")

# finally:
#     print("bhosda")




