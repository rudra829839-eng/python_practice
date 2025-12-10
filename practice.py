
# #  a  p    n   a   _   c   o   l   l   e   g    e
# #  -12 -11 -10 -9 -8  -7   -6  -5 -4  -3   -2   -1

# str = "apna_college"
# print(str[-12:-3])
# print(str[-10:-5])
# print(str[-8:-4])
 
#  #string Function
#  #num1 str.endswith("er.") =( return true if string ends with substr)
# str = " i am a studing  python from selfstkuding"
# print(str.endswith("ege"))

# #num2 str.capitalize = 1st charecter
# str1 = "i  am the very best"
# print(str1.capitalize())

# #num3  str.replace(old, new)
# str2 = "i  am the very best"
# print(str2.replace("the","bets"))
# print(str2.replace("am","bets"))
# print(str2.replace("i","bets"))

# #num4 str.find(word ) = 1st index of 1st occurrer
# str3 = "i  am the very best"
# print(str3.find("e"))

# #num5 str.cont("am")

# str4 = "i  am the very best"
# print(str.count("am"))

# # 1st question = WAP to input user frist name & print its length.

# name = input("enter your name:")
# print("lenth of your name is :",len(name))

# # WAP to find the occurrencen of '$' in a string

# str5 = "i $  am the $ very $ best"
# print(str5.count("$"))


#condition statements
age = int(input("enter your age"))

if age >= 18 :
    print("agree")
else:
    print("not agree")

light = input("enter colure light:")

if  (light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
else(light == "yellow"):
    print("ready")