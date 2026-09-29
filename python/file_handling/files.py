
'''creating file as myfile'''

# f=open("myfile.txt","w")
# data='''hello everyone how are you 
# my name is ankit prajapati 
# dosto kaise ho aap'''
# f.write(data)
# f.close()


'''reading that file '''

# f=open("myfile.txt","r")
# data=f.readlines()
# for i in data:
#     print(i)
# f.close()


'''appending the file'''

# with open("myfile.txt","a") as f:
#     f.write("\ntwinkle twinkle title star")
#     f.close()

# with open("myfile.txt","r") as f:
#     data=f.read()
#     if ("twinkle" in data):
#         print("present")
#     else:
#         print("absent")

'''create a program to update new high score into the file'''

# import random

# def game():
#     print("----you are playing the game----")
#     score=random.randint(1,100)

#     f=open("high_score.txt","r")
#     hiscore=f.read()
#     if(hiscore==""):
#         hiscore=0
#     else:
#         hiscore=int(hiscore)
#     f.close()

#     print("your score=",score)
#     if(score>hiscore):
#         f=open("high_score.txt","w")
#         f.write(str(score))
#         f.close()
# game()

'''writing table 1 to 20 in a folder of different files'''

# def generate_table(n):
#     table=""
#     for i in range(1,11):
#         table+= (f"{n} X {i} = {n*i}\n")

#     f=open(f"tables/table_{n}.txt","w")
#     f.write(f"\nTABLE OF {n}\n\n")
#     f.write(table)

# for i in range(1,21):
#     generate_table(i)



'''counting the number of words apper in the file'''

f=open("myfile.txt","r")
data=f.read()
count=data.count("twinkle")
print("occurance=",count)