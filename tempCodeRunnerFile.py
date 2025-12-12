print("rudra")
# condition statements
    #grade students based on marks
marks = int(input("enter your marks :"))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "fail"

age = int(input("enter your age : "))
if age >= 18:
    print("a")

else:
    print("b")

    Even or odd number check
progra number =1;
num = int(input("enter a number: "))
if num % 2 == 0:
    print("even Number") 
else:
    print("odd number")   

    #program number =2;
    # cheak the age (Minor/Adult)
    age = int(input("Enter your age"))
    if age >= 18:
        print("Adult")
    else:
        print("Minor")    
# program number = 3:
    #Twe largests number
a = int(input("enter a frist num"))
b = int(input("enter a second num")) 
if a > b: 
        print("grade num")
else:
        print("not grade")

# program number = 4 
# positive / Negetive/ Zero

num = int(input("enter number"))

if num < 0:
    print("negetive")
elif num > o:
    print("positive")
else:
    print("Zero")        

list [str,float,int,etc]
#program number 1 
marks1 = 94.5
marks2 = 76
marks3 = 47
marks4 = 78
marks5 = 56

marks = [94.5, 76, 47, 78,56]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(marks[3])
print(list(marks))
print(len(marks))

#program 2

student = [ "Rudra",18, "bihar", "kaimur"]
print(list(student))
print(student[0])
student[0] = "hearker rudra" 
print("new str list:", student)

marks = [85,97,767,8,6,66]
print(marks[0:4])
print(marks[2:5])
print(marks[0:])
print(marks[:5])

#list methods
list = [5,5,25,585,5565,65,5556,265,255,8,2,5258,2]
list.append(4)
print(list)

print(list.sort())
print(list)

list = [9,76,6,546,456,64367]
print(list.sort())
print(list)
 
list = [5,5,25,585,5565,65,5556,265,255,8,2,5258,2]
list.reverse()
print(list) 

list = [85,97,767,8,6,66]
list.insert(85,1000)
print(list)

#remove methods
list = [3,4,2,5,6,7,9,1]
list.remove(3)
print(list)
list.pop(2)
print(list)

#tupel methords
tup = (3,45,8,23,87,5)
print(type(tup))
print(tup[0])
print(tup[3])
print(type(tup))
print(tup[1:4])
print(tup[2:5])

#WAP to ask the user to enter names of thrir 3 favorite movies & store them in a list

movies = []
mov1 = input("Enter 1st movie")
mov2 = input("Enter 2nd movie")
mov3 = input("Enter 3rd movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)