#str= (input("Enter a string: "))
# def decr_rev_str(str):
#     new_str=""
#     for i in range(len(str)-1, -1, -1):
#         new_str= new_str+ str[i]
#     return new_str

# print(decr_rev_str(str))

# def incr_rev_str(str):
#     new_str=""
#     for i in range(len(str)):
#         new_str=  str[i] +new_str
#     return new_str

# print(incr_rev_str(str))


##incementing reccursion
# def recc_rev_str(str,i,new_str=""):
#     if i==len(str):
#         return new_str
#     new_str=  str[i] +new_str
#     return recc_rev_str(str,i+1,new_str)    

# print(recc_rev_str(str,0,new_str=""))


##decrementing 
# def recc_rev_str(i,new_str):
#     if i<0:
#         return new_str
#     new_str= new_str+ str[i] 
#     return recc_rev_str(i-1,new_str)    

# print(recc_rev_str(len(str)-1,new_str=""))


##string to list
# def list_str(str):
#     l=[]
#     for i in range(len(str)):
#         l.append(str[i])

#     return l
# print(list_str(str))


##string to reverse list
# def list_str(str):
#     l=[]
    
#     for i in range(len(str)):
#         l.append(str[i])
#     print(l)


#     i, j= 0, len(str)-1
#     while i <=j:
#         l[i], l[j]= l[j], l[i]
#         i+=1
#         j-=1
#     print(l)
    

#     new_str=""
#     for i in l:
#         new_str= new_str+ i

#     return new_str

# print(list_str(str))




# def list_str(str):
#     l=[]
    
#     for i in range(len(str)):
#         l.append(str[i])
#     print(l)


#     i, j= 0, len(str)-1
#     while i <=j:
#         l[i], l[j]= l[j], l[i]
#         i+=1
#         j-=1
#     print(l)
    

#     new_str=""
#     for i in l:
#         new_str= new_str+ i

#     return new_str

# print(list_str(str))





# import pickle
# class Employee:
#     def __init__(self, name, age, addr):
#         self.ename= name
#         self.eage= age
#         self.eaddr= addr

#     def disp(self):
#         print(self.ename)
#         print(self.eage)
#         print(self.eaddr)
# # e=Employee("Rakshi",21,"HSN")
# # f= open("serial.txt", "wb")
# # pickle.dump(e,f)
# # print("Object is stored in a file")
# # f.close()
# f= open("serial.txt", "rb")
# e=pickle.load(f)
# e.disp()
# print("from file object is retrived")


# s= input("Enter a string: ")
# def toLowerCase( s: str) -> str:
#     str=""
#     for i in range(len(s)):
#         if "A"<=s[i]<="Z":
#             str=  str + (chr(ord(s[i])+32)) 
#         else:
#             str= str +(s[i]) 
#     return str

# print(toLowerCase(s))



s=input("Enter a string: ")
def reverseWords(s):
        # code here 
    nw,ns="", ""
    s= s+" "
    for i in range (len(s)):
        if ("A" <= s[i]<= "Z") or ("a" <= s[i]<= "z"):
            nw=s[i]+nw
                
        elif nw!="":
            if ns!="":
                ns= ns+" " +nw

            else:
                ns= ns +nw
                    
            nw=""
                
    return ns

print(reverseWords(s))