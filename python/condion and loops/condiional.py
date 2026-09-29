
# checking the user age is able to vote or not

# age=int(input("enter the age :"))
# if(age>=18):
#     print("eligible for vote")
# elif(age<=0):
#     print("invalid age")
# else:
#     print("not eliglible for vote")




#checking the student is pass or fail 40% and in each subject required 33%

# sub1=int(input("enter the marks of sub1 :"))
# sub2=int(input("enter the marks of sub2 :"))
# sub3=int(input("enter the marks of sub3 :"))

# per=(sub1+sub2+sub3)/3
# if(per>=40 and sub1>=33 and sub2>=33 and sub3>=33):
#     print("student is pass, percentage is:",per)
# else:
#     if(sub1<33):
#         print("fail in sub1")
#     if(sub2<33):
#         print("fail in sub2")
#     if(sub3<33):
#         print("fail in sub3")

#     print("student is fail, and percentage is:",per)




# checkin the spam or not in comment section

# s1="buy now"
# s2="click here"
# s3="subscribe this"
# s4="click to collect gift"

# comment=input("enter the comment :")
# if((s1 in comment) or (s2 in comment) or (s3 in comment) or (s4 in comment)):
#     print("spam don't trust")
# else:
#     print("you can trust its not a spam")




#checking the lengh of user input name whether it is grater than 10 or not

# name=input("enter you name :")
# length=len(name)
# if(length<10):
#     print("name length is less than 10 and it is:",length)
# else:
#     print("name length is greater than or equal to 10 and it is:",length)



# to check the name in list or not

l=["ankit","aman","mummy","papa"]
check=input("enter the name :")
if(check.lower() in l.lower()): print("mera babu hai")
else: print("mera babu nhi hai")