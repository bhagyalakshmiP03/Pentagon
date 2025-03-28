# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# arr=createlist()
# n=len(arr)
# def ascending_sort(arr):
#     temp=0
#     for i in range(0,n-1):
#         for j in range(0,n-i-1):
#             if arr[j]> arr[j+1]:
#                 temp=arr[j+1]
#                 arr[j+1]=arr[j]
#                 arr[j]=temp

#     return arr

# res=ascending_sort(arr)
# print(res)



# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# arr=createlist()
# n=len(arr)
# def desending_sort(arr):
#     temp=0
#     for i in range(0,n-1):
#         for j in range(0,n-i-1):
#             if arr[j]<arr[j+1]:
#                 temp=arr[j+1]
#                 arr[j+1]=arr[j]
#                 arr[j]=temp

#     return arr

# res=desending_sort(arr)
# print(res)




#insertion sort
# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# arr=createlist()
# n=len(arr)
# def insetion_acssort(arr):
#     for i in range(0,n-1):
#         for j in range(i+1,0,-1):
#             if arr[j]<arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
#     return arr

# def insetion_descsort(arr):
#     for i in range(0,n-1):
#         for j in range(i+1,0,-1):
#             if arr[j]>arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
#     return arr

# res=insetion_acssort(arr)
# print("asc order : ",res)

# ress=insetion_descsort(arr)
# print("desc order :", ress)


##min value
def createlist():
    l=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l.append(n)
        except Exception as e:
            break
    return l

arr=createlist()
def min_value(arr):
    for i in range(0,len(arr)):
        min_val=arr[0]
        if arr[i]<min_val:
            min_val=arr[i]
    return min_val

