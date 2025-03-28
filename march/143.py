# l1=[]
# def fun1():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# arr=fun1()
# target=int(input("Enter a target no to search : "))

# a=len(l1)
# def linearsearch(arr,target):

#     for i in range(0,a):
#         if arr[i]==target:
#             return True , i 
#     return False, -1 
# flag, index= linearsearch(arr, target)     
# if flag==True:
#     print(target, " is found at index: ",index)
# else:
#     print("not found")

# lsr=linearsearch(arr,target)







# l1=[]
# def createlist():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# arr=createlist()

# print(arr)
# def revlist(arr):
#     i,j=0,len(arr)-1
#     while i<=j:
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
#         j-=1
#     return arr
# flag=revlist(arr)
# print(arr)




# l1=[]
# def createlist():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# arr=createlist()

# print(arr)
# def revlist(i, j,arr):
#     if i>j:
#         return arr
#     while i<=j:
#         arr[i],arr[j]=arr[j],arr[i]
#     return revlist(i+1,j-1,arr)

# flag=revlist(0,len(arr)-1,arr)
# print(flag)


l1=[]
def createlist():
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            break
    return l1

arr=createlist()

l2=[]
def revlist(arr):
    for i in range((len(arr)-1),-1,-1):
        l2.append(arr[i])
    return l2
print("Before rev:", arr)
revlist(arr)
print("After rev:", l2)