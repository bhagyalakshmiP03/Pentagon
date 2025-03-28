# comprison operator
print(5<10)
print((-15)>(-25))
print((10*3)!= 1000)
print((True* True)== (1//1))
print((10//2)<=(10*2))
print((5*5)>=(625*5))
print((10*10)>=(1000//10))

print((5.555)>(5.55))



#logical operator
# logical and
print((10+5) and (2*3) and (10**0))
if(-15 and -10):
    print("True")
else:
    print("False")

#logical or
print((10+5) or (2*3) or (10**0))
print((False or False or True))
print((10+9) or (8+9))

print((True and True)or (False and 15))
print(( False and 15) or (False and False))

#logical not
print(not(True and False))
print(not(10+5))

#bitwise operator
print(10&5)
print(10|5)
print(10^5)
print(~10)
print(10<<2)
print(10>>2)


# assignment operator
h=10
g=10
print(h==g)
print(id(h is g))
print(id(h and g))
print(id(h or g))



#Arithmetc operator
a=5
b=10
a=a+b
print(a)

a=5
a+=10
print(a)

x=5
x=x**(2+1)
print(x)
#Should be initialized before using
# c=c+(3*6)
# c+=3*6 
