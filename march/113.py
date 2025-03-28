# n=int(input())
# for i in range(0,n):
#     num=1
#     for j in range(0,i+1):
#         print(num,end="")
#         num=num*(i-j)//(j+1)
#     print()



# n=int(input())
# for i in range(0,n):
#     num=1
#     for k in range(n,i-1,-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print(num,end=" ")
#         num=num*(i-j)//(j+1)
#     print()



# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# n=int(input())
# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n=int(input())
# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==j or i+j==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# n=int(input())
# if n%2==0:
#     n=n+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or i==j or i+j==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



# n=int(input())

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==n or i==j :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# n=int(input())

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==1 or i+j==n+1 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



# n=int(input())

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==1 or j==n :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#hallow triangle
# n=int(input())
# noc=n
# nor=n
# for i in range(1,n+1):

#     for j in range(1,n*2):
#         if j==noc or j==nor or i==n : 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i <n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1



# n=int(input())
# noc=1
# nor=(n*2)-1
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if j==noc or j==nor or i==1: 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i <n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1


#hallow diamond
# n=int(input())
# noc=n
# nor=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if j==noc or j==nor:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i <n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1



#hallow k
# n=int(input())
# noc=n
# for i in range(1,n*2):
#     for j in range(1,n+1):

#         if i==1 or i==(n*2)-1 or j==1 or i-j==n-1 or i+j==n+1 :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1


#hallow rev k

# n=int(input())
# ### noc=1
# for i in range(1,n*2):
#     for j in range(1,n+1):
#         if i==1 or i==(n*2)-1 or j==n or i==j or i+j==n*2 :
#             print("*", end="")
#         else:
#             print(" ", end="")

#     for k in range (1,j):
#         print(" ",end="")
#     print()
#    ## # if i<n:
#     ###     noc+=1
#     ### else:
#     #  ##   noc-=1


# n=int(input())

# for i in range(1,n*2):
#     for j in range(1,n+1):
#         if i==j or i+j==n*2 or j==1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# n=int(input())

# for i in range(1,n*2):
#     for j in range(1,n+1):
#         if j==n or i+j==n+1 or i-j==n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





# n=int(input("ENter a num: "))
# for i in range(1,n+1):
#     for k in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()


n=int(input("ENter a num: "))
for i in range(1,n+1):
    for k in range(1,n,-1):
        print(" ",end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*", end="")
        else:
            print(" ",end="")
    print()

