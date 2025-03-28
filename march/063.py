n= int(input("Enter a range: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end="")
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end="")
#     print()


# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(count,end=" ")
#         count+=1
#     print()


count=1
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(i,n+1):
        print(count,end="")
        count+=1
    print()


