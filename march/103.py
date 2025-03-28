# n=int(input("enter a num: "))
# count1=1

# for i in range(1,n+1):
    
#     for j in range(1,i+1):
#         if i%2!=0:
#             print(count1, end=" ")
#             count2=count1
#         else :
#             print(count2+1, end=" ")
#             count2-=1
#         count1+=1
        
#     print()
#     count2=count2+i




# n=int(input())

# noc=1
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(j,end="")
    
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1    



n=int(input())
noc=n
temp=n
for i in range(1,n*2):
    for k in range(n,noc+1,-1):
        print(" ", end="")
    for j in range(1,noc+1):
        print(n,end="")
        n-=1
    print()
    n=temp
    if i<n:
        noc-=1
    else:
        noc+=1

