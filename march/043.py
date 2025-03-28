# n=int(input("Enter a no: "))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*", end="")
#     print()


# n=int(input("Enter a no: "))
# for i in range(1,n+1):
#     for k in range(1,i+1):
#         print(" ", end="")
#     for j in range(n,i-1,-1):
#         print("*", end="")
#     print()


# n=int(input("Enter a no: "))
# for i in range(1,n+1):
#     for k in range(1,i+1):
#         print(" ", end="")
#     for j in range(n,i-1,-1):
#         print("* ", end="")
#     print()




# n=int(input("Enter a no: "))
# noc=1
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print("+",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1


# n=int(input("Enter a no: "))
# noc=1

# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#         print("+",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
   


# n=int(input("Enter a no: "))
# noc=1

# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#         print("+ ",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1



#k shape
# n=int(input("Enter a no: "))
# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print("+",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1




# k rev shape
# n=int(input("Enter a no: "))
# noc=n
# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#         print("+",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1







# k rev shape
# n=int(input("Enter a no: "))
# noc=n
# for i in range(1,n*2):
#     for k in range(n,noc,-1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#         print("+ ",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1


n=int(input("Enter a no: "))
noc=1
nor=(n*2)-1

for i in range(1,n*2):
    for j in range(1,n*2):
        if (j<=noc or j>=nor):
            print("+",end="")
        else:
            print(" ", end="")
    print()
    if i<n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1
