# s=input("Enter a string : ")
# def stack(s):
#     stack=[]
#     for i in range(len(s)):
#         if s[i]=="(":
#             stack.append(")")
#         elif s[i]=="{":
#             stack.append("}")
#         elif s[i]=="[":
#             stack.append("]")
#         elif len(stack)==0 or s[i]!= stack.pop():
#             return False
            
#     return len(stack)==0

# print(stack(s))


def createlist():
    l=[]
    while True:
        try:
            n=int(input("ENter a no: "))
            l.append(n)
        except Exception as e:
            break
    return l

nums= createlist()

# def subarray(arr):
    
#     for i in range(len(arr)):
#         res=[]
#         for j in range(i,len(arr)):
#             res.append(arr[j])
#             print(res)
        
        
# (subarray(arr))






# def subarray(arr):
#     res=[]
#     for i in range(len(arr)):
#         subres=[]
#         for j in range(i,len(arr)):
#             subres.append(arr[j])
#             res.append(subres)
#     return res
        
# arr= createlist()     
# print(subarray(arr))
    


def threeSum( nums):
    a=[]
    for i in range(len(nums)):
        
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                b=[]
                if nums[i] +nums[j]+nums[k]==0:
                    b.append([nums[i],nums[j],nums[k]])
                    a.append(b)

    return a