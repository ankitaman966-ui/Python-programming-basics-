'''create class programmer detail working in microsoft'''

# class programmer:
#     company="microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# p=programmer("ankit",120000,226401)
# print(f'''Company= {p.company}\nName= {p.name}\nSalary= {p.salary}\npin= {p.pin}''')



'''making a class calculator '''

# class calculator:
#     def __init__(self,n):
#         self.n=n

#     def square(self):
#         print(f"square of the givern number is :{self.n*self.n}")

#     def cube(self):
#         print(f"the cube of the given number is: {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"sqaureroot of the given number :{self.n**0.5}")

# a=calculator(5)
# a.square()
# a.cube()d# a.squareroot()




'''create a prgramme  to book the ticket of train  that will show train detail like no. and  
       fare and current status and show the train destinatin and departure'''

# import random

# class train:

#     def __init__(self,train_no,fro,to):
#         self.train_no=train_no
#         self.fro=fro
#         self.to=to

#     def book(self):
#         print()
#         print(f"ticket is booked in train no : {self.train_no} form {self.fro} to {self.to}")

#     def status(self):
#         print(f"Train no :{self.train_no} is running on time")

#     def fare(self):
#         print(f"ticket fare for the train no :{self.train_no} from {self.fro} to {self.to} is {random.randint(100,1000)}")

# t=train(226401,"lucknow","Azamgarh")
# t.book()
# t.fare()
# t.status()