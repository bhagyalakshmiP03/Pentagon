# num=int(input("Enter a number: "))
# if num%2==0:
#     print(num," is Even")
# else:
#     print(num, " is odd")


##using function
# def checkEvenOdd(num):
#     if num%2==0:
#         return True
#     return False

# n=int(input("Enter a num: "))
# flag= checkEvenOdd(n)

# if flag:
#     print(n, "is even")
# else:
#     print(n, "is odd")


##optimization of code..
# def checkEvenOdd(num):
#     return num%2==0

# n=int(input("Enter a num: "))
# flag= checkEvenOdd(n)

# if flag:
#     print(n, "is even")
# else:
#     print(n, "is odd")


## here we are directly passing the logic without storing it variable.. this is bad bcz we can't reuse it
# def checkEvenOdd(num):
#     return num%2==0

# n=int(input("Enter a num: "))
# if checkEvenOdd(n):
#     print(n, "is even")
# else:
#     print(n, "is odd")


## resusing the function
# def checkEvenOdd(num):
#     return num%2==0

# sr= int(input("Enter a start value: "))
# er= int(input("Enter a end value: "))

# if sr <=er:
#     print("Even num: ")
#     for i in range(sr, er+1, +1):
#         if checkEvenOdd(i):
#             print(i)
# else:
#     print("Invalid input") 




##using Not
# def checkEvenOdd(num):
#     return num%2==0

# sr= int(input("Enter a start value: "))
# er= int(input("Enter a end value: "))


# if sr <=er:
#     print("Even num: ")
#     for i in range(sr, er+1, +1):
#         if checkEvenOdd(i):
#             print(i)
#     print("Odd num: ")
#     for i in range(sr,er+1):
#          if not checkEvenOdd(i):
#               print(i)
         
# else:
#         print("Invalid input") 
   


##using true or false
# def checkEvenOdd(num):
#     return num%2==0

# sr= int(input("Enter a start value: "))
# er= int(input("Enter a end value: "))


# if sr <=er:
#     print("Even num: ")
#     for i in range(sr, er+1, +1):
#         if checkEvenOdd(i)==True:
#             print(i)

#     print("Odd num: ")
#     for i in range(sr,er+1):
#          if checkEvenOdd(i)==False:
#               print(i)
         
# else:
#         print("Invalid input") 
   
    
##using 0 or 1
# def checkEvenOdd(num):
#     return num%2==0

# sr= int(input("Enter a start value: "))
# er= int(input("Enter a end value: "))


# if sr <=er:
#     print("Even num: ")
#     for i in range(sr, er+1, +1):
#         if checkEvenOdd(i)==1:
#             print(i)
#     print("Odd num: ")
#     for i in range(sr,er+1):
#          if checkEvenOdd(i)==0:
#               print(i)
         
# else:
#         print("Invalid input") 
   




def checkEvenOdd(num):
    return num%2==0
sr=1
er= int(input("Enter n number: "))


if sr <=er:
    print("Even num: ")
    for i in range(sr, (er*2)+1):
        if checkEvenOdd(i):
            print(i)
         
else:
        print("Invalid input") 
   