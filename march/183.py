
# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def merge(l1,l2):
#     i,j,k=0,0,0
#     res=[]
#     while k< len(l1) +len(l2):
#         if i <len(l1) and k%2==0:
#             res.append(l1[i])
#             i+=1
#             k+=1
#         elif j< len(l2) and k%2!=0:
#             res.append(l2[j])
#             j+=1
#             k+=1
#         elif j<len(l2):
#             res.append(l2[j])
#             j+=1
#             k+=1
#         else :
#             res.append(l1[i])
#             i+=1
#             k+=1
#     return res


# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=merge(l1,l2)
# print(ress)



###ascending merg
# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=0,0
#     while i<len(l1) and j<len(l2):
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j+=1

#     while i<len(l1):
#         res.append(l1[i])
#         i+=1
#     while j<len(l2):
#         res.append(l2[j])
#         j+=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)




#decesending merge
# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergedsc(l1,l2):
#     res=[]
#     i,j=0,0
#     while i<len(l1) and j<len(l2):
#         if l1[i]>l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j+=1

#     while i<len(l1):
#         res.append(l1[i])
#         i+=1
#     while j<len(l2):
#         res.append(l2[j])
#         j+=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergedsc(l1,l2)
# print(ress)




###decesending to ascending

# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=(len(l1)-1),(len(l2)-1)
#     while i>=0 and j>=0:
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i-=1
#         else:
#             res.append(l2[j])
#             j-=1

#     while i>=0:
#         res.append(l1[i])
#         i-=1
#     while j>=0:
#         res.append(l2[j])
#         j-=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)


###ascending to descending
# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=(len(l1)-1),(len(l2)-1)
#     while i>=0 and j>=0:
#         if l1[i]>l2[j]:
#             res.append(l1[i])
#             i-=1
#         else:
#             res.append(l2[j])
#             j-=1

#     while i>=0:
#         res.append(l1[i])
#         i-=1
#     while j>=0:
#         res.append(l2[j])
#         j-=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)


# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=0,(len(l2)-1)
#     while i>=len(l1) and j>=0:
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j-=1

#     while i>len(l1):
#         res.append(l1[i])
#         i+=1
#     while j>=0:
#         res.append(l2[j])
#         j-=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)


# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=0,(len(l2)-1)
#     while i<len(l1) and j>=0:
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j-=1

#     while i<len(l1):
#         res.append(l1[i])
#         i+=1
#     while j>=0:
#         res.append(l2[j])
#         j-=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)





# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l.append(n)
#         except Exception as e:
#             break
#     return l

# def mergeasc(l1,l2):
#     res=[]
#     i,j=0,(len(l2)-1)
#     while i<len(l1) and j>=0:
#         if l1[i]>l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j-=1

#     while i<len(l1):
#         res.append(l1[i])
#         i+=1
#     while j>=0:
#         res.append(l2[j])
#         j-=1
#     return res

# l1=createlist()
# l2=createlist()
# print(l1)
# print(l2)
# ress=mergeasc(l1,l2)
# print(ress)







def createlist():
    l=[]
    while True:
        try:
            n=int(input("enter the number:"))
            l.append(n)
        except Exception as e:
            break
    return l
def first_max(arr):
    max=-2147483648
    maxindex=-1
    secmax=-2147483648
    secmaxindex=-1
    for i in range(len(arr)):
        if max<arr[i]:
            secmax=max
            secmaxindex=maxindex
            max=arr[i]
            maxindex=i
        elif max!=arr[i] and secmax<arr[i]:
            secmax=arr[i]
            secmaxindex=i
    return [max,maxindex,secmax,secmaxindex]
arr=createlist()
res=first_max(arr)
print("first maximum",res[0],"at",res[1])
print("second maximum",res[2],"at",res[3])