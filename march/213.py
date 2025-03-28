
def createlist():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            break
    return l1



# def ceilingtargetasc(arr,target):
#     start,end=0,len(arr)-1
    
    
#     if arr[start]>target>arr[end]:
#         return -1
#     while start<end:
#         mid=(start+end)//2
#         if target==arr[mid]:
#             return arr[mid]
#         if target < arr[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     return arr[start]

# arr=createlist()
# target=int(input("Enter a target no: "))
# res=ceilingtargetasc(arr,target)
# print(res,i)



#error
# def ceilingtargetdsc(arr,target):
#     start,end=len(arr)-1,0
    
    
#     if target>arr[end]or arr[start]:
#         return -1
#     while start>end:
#         mid=(start+end)//2
#         if target==arr[mid]:
#             return arr[mid]
#         if target < arr[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     return arr[start],start

# arr=createlist()
# target=int(input("Enter a target no: "))
# res=ceilingtargetdsc(arr,target)
# print(res)



def floorsearch(arr,target):

    start,end=0,len(arr)-1
    
    
    if arr[end]<target<arr[start]:
        return -1
    while start<end:
        mid=(start+end)//2
        if target==arr[mid]:
            return arr[mid]
        if target < arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return arr[end]

arr=createlist()
target=int(input("Enter a target no: "))
res=floorsearch(arr,target)
print(res)