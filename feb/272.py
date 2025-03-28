# n=4


# def dispnum4(n):
#     print(n)
#     dispnum3(n-1)

# def dispnum3(n):
#     print(n)
#     dispnum2(n-1)


# def dispnum2(n):
#     print(n)
#     dispnum1(n-1)

# def dispnum1(n):
#     print(n)
    
# dispnum4(4)





# def dispnum(n):
#     if n<=0:
#         return
    
#     dispnum(n-1)
#     print(n)

# n=int(input("enter a num : "))
# dispnum(n)






# def dispnum(n):
#     if n<=0:
#         return
#     print(n)
#     dispnum(n-1)
#     print(n)

# n=int(input("enter a num : "))
# dispnum(n)


# input: 4
# output: 12344321

# def dispnum(n,i=1):
#     if i>n:
#         return
#     print(i,end="")
#     dispnum(n,i+1)
#     print(i,end="")

# n=int(input("ENter a num: "))
# dispnum(n)

    



# n=int(input("enter a num : "))
# dispnum(n)





#recursive count
# count=0
# def countdigrecc(n, count):
#     if n==0 or n==-1:
#         return count
#     n//=10
#     count+=1
#     return countdigrecc(n,count)
# n=int(input("ENter a number :"))
# res=countdigrecc(n,count)
# print(res)





def countdigrecc(n, count=0):
    flag=True
    if n<0:
        n=n*-1
        flag=False
    if n<=0:
        return count
    n//=10
    count+=1
    return countdigrecc(n,count)

n=int(input("ENter a number :"))

res=countdigrecc(n)
# if n==-1:
#     print(1)
# else:    
print(res)





#recursive fibinocii

# def fibirecc(pos,n1,n2):
#     if pos<=0:
#         return