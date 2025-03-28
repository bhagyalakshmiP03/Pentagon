# 
# # using for- factors
# num=int(input("ENter a number : "))

# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=",")

# 


# using while factor
#  num=int(input("ENter a number : "))
# i=1
# while i*i<=num:
#     if num%i==0:
#         print(i)
#         fact2=num//i
#         if (fact2) !=i:
#             print(fact2)
#     i=i+1 





##w.a.p to check whether prime or not

####def printfactors(num):
    # i=1
    # while i*i<=num:
    #     if num%i==0:
    #         print(i,end=" ")
    #         fact2=num//i
    #         if (fact2) !=i:
    #             print(fact2)
    #     i=i+1 

# def isprime(num):
#     i=2
#     while i*i<=num:
#         if num%i==0:
#             return False
#         i=i+1
#     return True     

# num=int(input("ENter a number : "))
# ##print("Factors: ")
# ##printfactors(num)
# ##print("===============")
# flag=isprime(num)
# if flag==True:
#     print(num," is a prime")
# else:
#     print(num," is not a prime")




#First N prime numbers
# def is_prime(num):
#     if num < 2:
#         return False
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             return False
#         i += 1
#     return True

# def n_prime(n):
#     count = 0
#     num = 2
#     print(" prime numbers are:")
#     while count < n:
#         if is_prime(num):
#             print(num, end=" ")
#             count += 1
#         num += 1

# n = int(input("Enter how many prime num u want : "))
# n_prime(n)





#GCD / HCF of 2 number
# n1=int(input("Enter a num1: "))
# n2= int(input("Enter a num2: "))
# hcf=1
# if n1<=n2:
#     for i in range(1, n1+1):
#         if n1%i==0 and n2 % i==0:
#             hcf=i
# else:
#     for i in range(1, n2+1):
#         if n1%i==0 and n2% i==0:
#             hcf=i
# print(hcf)



##using for
# n1=int(input("Enter a num1: "))
# n2= int(input("Enter a num2: "))
# hcf=1
# if n1<=n2:
#     n1,n2 = n2,n1
# for i in range(1, n1+1):
#     if n1%i==0 and n2 % i==0:
#         hcf=i
# print(hcf)




###using while
# n1=int(input("Enter a num1: "))
# n2= int(input("Enter a num2: "))

# hcf=1
# i=1
# while i<=n1:
#     if (n1%i==0 and n2%i==0):
#         hcf=i
#     i+=1
# print(hcf)

# ###using function
# def dispHcf(n1,n2):
#     hcf=1
#     if n1<=n2:
#         n1,n2=n2,n1
#     for i in range(1, n1+1):
#         if n1%i==0 and n2 % i==0:
#             hcf=i
#     return hcf

# res=dispHcf(n1,n2)
# print(res)




#calculating the Lcm of 2 numbers
def gcd(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    i = 1
    hcf = 1
    while i <= num1:
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
        i += 1
    return hcf  

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2) 
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm_value = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_value}")





##fibiocci series
# pos_num=int(input("enter a num: "))

# n1=0
# n2=1
# print(n1)
# print(n2)

# i=3
# while i<= pos_num:
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3
#     i+=1


# def fibinocci(pos_num):
#     n1=0
#     n2=1
#     i=1
#     if (i<=pos_num):
#         print(n1,end=" ")
#         i+=1
#     if(i<=pos_num):
#         i+=1
#         print(n2, end=" ")
        
#     while i<= pos_num:
#         n3=n1+n2
#         print(n3,end=' ')
#         n1=n2
#         n2=n3
#         i+=1

# pos_num=int(input("enter a num: "))

# fibinocci(pos_num)