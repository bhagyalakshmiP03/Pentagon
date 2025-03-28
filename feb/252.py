# ##fibinocii series in a single loop
# pos=int(input("Enter a position number: "))

# n1=0
# n2=1

# while pos!=0:
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     pos-=1


##in function
def fibi(pos):
    n1=0
    n2=1

    while pos!=0:
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3
        pos-=1
pos=int(input("Enter a position number: "))
fibi(pos)


##output  ending range
# def fibi(pos):
#     n1=0
#     n2=1

#     while pos!=1:
        
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         pos-=1
#     print(n1,end=" ")
# pos=int(input("Enter a position end number: "))
# fibi(pos)
