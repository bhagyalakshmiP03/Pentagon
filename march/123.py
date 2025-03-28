# l2=[]
# print(l2)   #[]
# print(len(l2))    #0

# ##l2[0]=10     #IndexError: list assignment index out of range

# l2.append(-3)
# print(l2)
# l2.insert(3,10) 
# print(l2) #internally acts as append if index is not in range
# l2.insert(2,33) 
# print(l2) #shift the exiting element to right hand side then insert the value
# l2[0]=4 
# print(l2)#insert directly when index exist in list
# l2.insert(0,1000)
# print(l2)



# l2.append("Abc")
# print(l2)
# l2.append([-2,-6])
# print(l2)
# l3=[25,36]
# print(l2)
# l2.extend(l3)

# print(l2)





# l1=[]
# while True:
#     try:
#         n=int(input("Enter a num: "))
#         l1.append(n)
#     except Exception as e:
#         break

# print(l1)


# #using fun
# l1=[]
# def fun1():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1
# f1=fun1()
# print(f1)




# l1=[]
# while True:
#     n=(input("enter a num: "))
#     if n=="":
#         break
#     else:
#         l1.append(n)
# print(l1)




# l1=[]
# def fun1():
#     while True:
#         n=(input("enter a num: "))
#         if n=="":
#             break
#         else:
#             l1.append(n)
#     return l1
# f1=fun1()
# print(f1)



#
#w r p to disp sum of all the elements of a given list
#w r p to disp product of all the elements of a given list
#w r p to  disp the diff of the product and sum of all the elements in a lists

#sum of in the list
# l1=[]
# def fun1():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# f1=len(fun1())

# def sumlist():
#     sum=0
#     for i in range(0,f1):
#         sum= sum + l1[i]
#     return sum

# s1=sumlist()
# print(s1)




#w r p to disp product of all the elements of a given list
# l1=[]
# def fun1():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:
#             break
#     return l1

# f1=len(fun1())
# def productlist():
#     pro=1
#     for i in range(0,f1):
#         pro= pro * l1[i]
#     return pro

# s1=productlist()
# print(s1)


#w r p to  disp the diff of the product and sum of all the elements in a lists

# l1=[]
# def fun1():
#     while True:
#         try:
#             n=int(input("Enter a num: "))
#             l1.append(n)
#         except Exception as e:

#             break
#     return l1

# f1=len(fun1())
# def sumlist():
#     sum=0
#     for i in range(0,f1):
#         sum= sum + l1[i]
#     return sum

# def productlist():
#     pro=1
#     for i in range(0,f1):
#         pro= pro * l1[i]
#     return pro

# s1=sumlist()
# print("sum of list : ", s1) 
# p1=productlist()
# print("product of list : ",p1 )
# print(("diff between pro and sum"),p1-s1)





l1=[]
def fun1():
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            break
    return l1


def sumlist(l1):
    sum=0
    for i in l1:
        sum= sum + l1[i]
    return sum

def productlist(l1):
    pro=1
    for i in l1:
        pro= pro * l1[i]
    return pro

f1=fun1()
s1=sumlist()
print("sum of list : ", s1) 
p1=productlist()
print("product of list : ",p1 )
print(("diff between pro and sum"),p1-s1)