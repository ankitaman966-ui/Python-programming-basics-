
''' create dictonary '''
# d={"name":"ankit","marks":98.4,"age":18}
# # print(d)
# # print(d.items())
# a=d.get("marks")
# print(a)
# # print(d.values())






''' creating dictionary and update value of student '''

# d={}

# def create():
#     while True:
#         print("enter the details of the student")
#         rollno=int(input("\nenter the rollno of the student:"))
#         name=input("enter the name of the student:")
#         marks=int(input("enter the marks of the student"))
#         d[rollno]={"name":name,"marks":marks}

#         ch=input("enter you want to enter more detail (y/n)")
#         if(ch=="N" or ch=="n"):
#             break

# def modify():
#     key=int(input("enter the roll no of the student to update the details :"))
#     for rollno in d:
#         if(key==rollno):
#             print(''' enter the change you want to made 
#                   both -> name and marks
#                   name -> name
#                   marks -> marks''')
#             change=input("enter the changes as per given parameter above :")

#             if(change=="both"):
#                 new_name=input("enter the new correct name of the student :")
#                 new_marks=int(input("enter the new marks of the student :"))
#                 d[rollno]["name"]=new_name
#                 d[rollno][new_marks]=new_marks

#             elif(change=="name"):
#                 new_name=input("enter the new correct name of the student :")
#                 d[rollno]["name"]=new_name

#             elif(change=="marks"):
#                 new_marks=int(input("enter the new marks of the student :"))
#                 d[rollno]["marks"]=new_marks
#         else:
#             print("invalid roll no ")
                

# def display():
#     print("\nSTUDENT DETAILS\n")
#     for i in d:
#         print(f"{i}-> {d[i]}")


# create()
# display()
# modify()
# display()
