# Logical Operators :-

a = True
b = False

print( a and b )  
print( a or b )


a = 10 
b = 20 

print("first condition:", a > b and b > a )
print("second condition:", a == b and a < b)
print( "third condition:", a < b or  b < a)



a = True 
b = False
print(not a)  # false 
print(not b)  # true


x = 22
y = 11

print("condition check: ", x < y)  # false
print("after not operator: ", not (x < y))  # True

print("after check multiple condition: ",x < y and x > y)  ## False 

print(not(x < y and x > y)) ## True

a = True
b = False

print( a and b )   #=> False
print( a or b )  #=> True 


a = 10 
b = 20 
print( a > b and b > a )

False and True  #=> False 

print( a == b and a < b)
       
False  and True #=> False 

print( a < b or  b < a)
True  or  False #=> True 
      

a = True 
b = False 
print(not b) #=> True
print(not a) #> False 


x = 22
y = 11

print(x < y)

print(x < y and x > y)  ## False 

print(not(x < y and x > y)) ## True

