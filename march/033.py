# for i in range(1, 4+1):
#     print('*', end =" ")


# for i in range(1, 4+1):
#     for j in range(1, 4+1):
#         print('*', end =" ")
#     print()


# for i in range(4,1-1,-1):
#     print('*', end =" ")




# for i in range(4,1-1,-1):
#     for j in range(4,1-1,-1):
#         print('*', end =" ")
#     print()



# n=int(input("ENter a num: "))
# if 4<=n<=15 :
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("+", end="")
#         print()
# else:
#     print("Invalid input")


# n=int(input("Enter a num: "))
# for i in range(1, n+1):
#     for k in range(n, i,-1):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print("+", end="")
#     print()   


# n=int(input("Enter a num: "))
# for i in range(1, n+1):
#     for k in range(n, i,-1):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print("+ ", end="")
#     print()   
 
n=int(input("Enter a num: "))
for i in range(1, n+1):
    for k in range(n, i,-1):
        print(" ", end="")
    for j in range(1,i*2):
        print("+", end="")
    print()   
 