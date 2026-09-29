
''' creating 2d and 3d class and print the vector using super constructor '''

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j")


# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
    
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

# a=TwoDVector(5,10)
# b=ThreeDVector(5,10,15)

# a.show()
# b.show()



''' creating the class animal and pet and dog class interconnect and add bark method to dog '''

# class Animals:
#     pass

# class pets(Animals):
#     pass

# class dog(pets):

#     @staticmethod
#     def bark():
#         print("bow bow")


# d=dog()
# d.bark()




''' creating class employee and print new salary increment and later increament using property  and setter'''

# class employee:
#     salary=300
#     increment=20

#     @property
#     def increasedsalary(self):
#         return (self.salary+ self.salary*(self.increment/100))
    
#     @increasedsalary.setter
#     def increasedsalary(self,salary):
#         self.increment = (salary/self.salary-1)*100
        

# e=employee()
# # print(e.increasedsalary)
# e.increasedsalary=400
# print(e.increment)



''' creating class ot solve mutiplication using overloaded operator '''

# class number:
#     def __init__(self,n):
#         self.n=n

#     def __add__(self,other):
#         addition = self.n + other.n
#         print(f"addtion of the two number is {addition} ")

#     def __mul__(self,other):
#         multi = self.n * other .n
#         print(f"multiplication of the two number is {multi}")

# num1=int(input("enter the number :"))
# num2=int(input("enter the number :"))
# n=number(num1)
# m=number(num2)

# n+m
# n*m



'''adding complex number in the in class and also multiplication'''

# class complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return complex(self.r + c2.r, self.i + c2.i)

#     def __mul__(self, c2):
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return complex(real, imag)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"


# c1 = complex(2, 5)
# c2 = complex(3, 4)

# print("Addition:", c1 + c2)
# print("Multiplication:", c1 * c2)


''' adding two vector'''

# class addition:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def vector1(self,x,y,z):
#         print(f" vector 1 is : {self.x}i {self.y}j {self.z}k")


# a=addition(2,4,6)
# a.vector1(2,4,6)