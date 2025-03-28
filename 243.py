# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("ENter a num :"))
#             l.append(n)

#         except Exception as e:
#             break
#     return l

# def finddup(arr):
#     dict={}

#     for i in range(len(arr)):
#         if arr[i] in dict:
#             arr[i]= arr[i]+1
#         else:
#             arr[i]=1

#     print("Duplicates: ")  
#     for key, value in dict.items():
#         if value >1:
#             print(key, end="")

#     print("\nunique: ")
#     for key, value in dict.items():
#         if value == 1:
#             print(key, end="")

#     print("\nNon Duplicates: ")
#     for key, value in dict.items():
#         if value >= 1:
#             print(key, end="")
            
            
# arr=createlist()
# finddup(arr)








#string
#Upper to lower

# str=input("ENter a string: ")


# def UpperToLower(str):
#     new_str=""
#     for i in range(len(str)):
#         if "A"<= str[i]<= "Z":
#             new_str= new_str + chr(ord(str[i])+32)
#         else:
#             new_str= new_str+ str[i]
#     return new_str

# def LowerToUpper(str):
#     new_str=""
#     for i in range(len(str)):
#         if "a"<= str[i]<= "z":
#             new_str= new_str + chr(ord(str[i])-32)
#         else:
#             new_str= new_str+ str[i]
#     return new_str

# def swapstr(str):
#     new_str=""
#     for i in range(len(str)):
#         if "A"<= str[i]<= "Z":
#             new_str= new_str + chr(ord(str[i])+32)
#         elif "a"<= str[i]<= "z":
#             new_str= new_str + chr(ord(str[i])-32)
#         else:
#             new_str= new_str+ str[i]
#     return new_str

# print("before convert : ",str,  "--------After Convert to lower: ", UpperToLower(str))
# print("before convert : ",str,  "--------After Convert to upper: ", LowerToUpper(str))
# print("before convert : ",str,  "--------After Convert to swap: ", swapstr(str))




# str=input("Enter a string: ")
# def sumdig(str):
#     sum=0
#     for i in range(len(str)):
#         if "0" <= str[i] <= "9":
#             sum= sum+( ord(str[i]) -48)
#     return sum

# print(sumdig(str))








# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("ENter a num :"))
#             l.append(n)

#         except Exception as e:
#             break
#     return l

# arr=createlist()
# brr=createlist()


# def missingNumbers(arr, brr):
#     # Write your code here
#     dict1={}
#     dict2={}
#     for i in range(len(arr)):
#         if arr[i] in dict1:
#             arr[i]= arr[i]+1
#         else:
#             arr[i]=1
#     for j in range(len(brr)):
#         if arr[j] in dict2:
#             arr[j]= arr[j]+1
#         else:
#             arr[j]=1
    
#     for key1, value1 in dict1.items():
#         for key2, value2 in dict2.items():
#             if value1== value2:
#                 continue
#             else:
#                 print(key1, end="")
#         # if key1 in dict2:
#         #     continue
#         # else:
#         #     print(key1, end="")



#         # if value1== value2:

#         #     continue
#         # else:
#         #     print(key1, end="")


    

# missingNumbers(arr, brr)







# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("ENter a num :"))
#             l.append(n)

#         except Exception as e:
#             break
#     return l

# arr=createlist()
# brr=createlist()
# a=[]
# dict1={}
# dict2={}
# for i in arr:
#     if i in dict1:
#         dict1[i]=dict1[i]+1
#     else:
#         dict1[i]=1
# for i in brr:
#     if i in dict2:
#         dict2[i]=dict2[i]+1
#     else:
#         dict2[i]=1
# if len(arr)>=len(brr):
#     n=len(arr) 
# else: 
#     n=len(brr)
# for i in brr:
#     if i in dict2 and i in dict1:
#         if dict2[i]!=dict1[i] and i not in a:
#             a.append(i) 
#     else:
#         a.append(i)
# print(sorted(a))






# def createlist():
#     l=[]
#     while True:
#         try:
#             n=int(input("ENter a num :"))
#             l.append(n)

#         except Exception as e:
#             break
#     return l

# arr=createlist()
# brr=createlist()


# def missingNumbers(arr, brr):
#     # Write your code here
#     dict1={}
#     dict2={}
#     for i in range(len(arr)):
#         if arr[i] in dict1:
#             arr[i]= arr[i]+1
#         else:
#             arr[i]=1
#     for i in range(len(brr)):
#         if arr[i] in dict2:
#             arr[i]= arr[i]+1
#         else:
#             arr[i]=1
    
#     for i in dict1 and i in dict2:
#         if dict1[i]==dict2[i]:
#             continue
#         else:
#             return i

# missingNumbers(arr, brr)




























































