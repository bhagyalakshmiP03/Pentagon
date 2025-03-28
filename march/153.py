#rhs shift array by k
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


# def revlist(i , j , arr):
#     if i>j:
#         return arr
#     arr[i],arr[j]=arr[j],arr[i]
#     return revlist(i+1,j-1,arr)

# k=int(input("ENter a rotate number"))
# if k >len(arr):
#     k=k%len(arr)
# print("original array",arr)
# revlist(0,len(arr)-1,arr)
# revlist(0,k-1,arr)
# revlist(k,len(arr)-1,arr)
# print("shift arr",arr)


# #lhs shift array by k
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

# def revlist(i , j , arr):
#     if i>j:
#         return arr
#     arr[i],arr[j]=arr[j],arr[i]
#     return revlist(i+1,j-1,arr)

# k=int(input("ENter a rotate number"))
# if k >len(arr):
#     k=k%len(arr)
# print("original array",arr)
# revlist(0,len(arr)-1,arr)
# revlist(0,k-2,arr)
# revlist(k-1,len(arr)-1,arr)
# print("shift arr",arr)

##Max ele
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


# def maxele(arr):
#     maxx=-2147483648
#     maxind=-1
#     for i in range(0,len(arr)):
#         if maxx<arr[i]:
#             maxx=arr[i]
#             maxind=i
#     return maxx, maxind
# flag=maxele(arr)
# print("Max element and its index in list:", flag)

#min
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


def minele(arr):
    min=2147483648
    minind=-1
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
            minind=i
    return min, minind
flag=minele(arr)
print("Min element and its index in list:", flag)