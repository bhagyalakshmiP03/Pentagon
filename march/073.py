#Alphabetic patterns:

n=int(input("enter a range: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(96+j), end="")
#     print()

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(chr(64+i), end="")
#     print()


# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         if i%2!=0:
#             print(chr(64+j),end="")
#         else:
#             print(chr(96+j),end="")
#     print()



# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         if i%2==0:
#             print(chr(96+j),end="")
#         else:
#             print(chr(64+j),end="")
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i+j)%2==0:
#             print(chr(64+j),end="")
#         else:
#             print(chr(96+j),end="")
#     print()

# noc=n
# for i in range(1,n*2):
#     for j in range(1, noc+1):
#         print(chr(64+j),end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
    



# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(chr(64+i),end="")
          
#         else:
#             print(chr(64+j),end="")
#     print()
    

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j>=i:
#             print(chr(96+i),end="")
#         else:
#             print(chr(96+j),end="")
#     print()



# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(chr(96+j),end="")
#         else:
#             print(chr(96+i),end="")
#     print()



# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if j<=i:
#             print(chr(96+i),end="")
#         else:
#             print(chr(96+j),end="")
#     print()


# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if j>=i:
#             print(chr(64+i),end="")
#         else:
#             print(chr(64+j),end="")
#     print()



# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()



# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if j<=i:
#             print(chr(64+i),end="")
#         else:
#             print(chr(64+j),end="")
#     print()



# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(chr(64+j),end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1


# noc=n
# nor=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if noc>=j :
#             print(chr(64+j))
#         elif j<nor:
#             print(chr(64+j),end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1


noc=n
nor=n
for i in range(1,n*2):
    for j in range(1,n+1):
        if noc>=j:  
            print(chr(64+j),end="")
        elif j<=nor :
            print(chr(64+j),end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
        nor+=1
    else:
        noc+=1
        nor-=1



