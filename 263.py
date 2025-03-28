#s= input("ENter a string: ")

# def revwordstr(s):
#     new_word=""
#     new_sen=""
#     s= s + " "
#     i=0
#     while i < len(s):
#         if ("A"<= s[i]<= "Z") or ("a"<= s[i]<= "z")  :
#             new_word= new_word+ s[i]
           
#         elif new_word!="":
#             if new_sen!="":
#                 new_sen= new_word + " " + new_sen

#             else:
#                 new_sen= new_word+ new_sen
#             new_word=""
#         i+=1
#     return new_sen

# print(revwordstr(s))

    

# def reverseWords(s):
#     new_word, new_sen= "", ""
#     s=s+" "
#     for i in range(len(s)):
#         if ("A"<=s[i]<="Z") or ("a"<=s[i]<="z") or ("'"):
#             new_word= s[i]+ new_word

#         elif new_word!="":
#             if new_sen!="":
#                 new_sen= new_sen + " " + new_word

#             else:
#                 new_sen= new_sen + new_word
#             new_word=""
#     return new_sen

# print(reverseWords(s))


# def revwordstr(s):
#     new_word=""
#     new_sen=""
#     s= s + " "
#     i=0
#     while i < len(s):
#         if ("A"<= s[i]<= "Z") or ("a"<= s[i]<= "z")  :
#             new_word= s[i] + new_word
           
#         elif new_word!="":
#             if new_sen!="":
#                 new_sen= new_sen + " " + new_word

#             else:
#                 new_sen= new_sen+ new_word
#             new_word=""
#         i+=1
#     return new_sen

# print(revwordstr(s))


# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         i,nwrd,nstr=0,'',''
#         str=title+' '
#         while i<len(str):
#             if str[i]!=' ':
#                 nwrd+=str[i]
#             else:
#                 if len(nwrd)<=2:
#                     nwrd=self.lower(nwrd)
#                 else:
#                     nwrd=self.capitalize(nwrd)
#                 if nstr!='':
#                     nstr=nstr+' '+nwrd
#                     nwrd=''
#                 else:
#                     nstr+=nwrd
#                     nwrd=''
#             i+=1
#         return nstr
#     def lower(self,str):
#         res=''
#         for i in str:
#             if 'a'<=i<='z':
#                 res+=i
#             else:
#                 res+=(chr(ord(i)+32))
#         return res
#     def capitalize(self,str):
#         res=''
#         if 'a'<=str[0]<='z':
#             res+=chr(ord(str[0])-32)
#         else:
#             res+=str[0]
#         for i in range(1,len(str)):
#             if 'a'<=str[i]<='z':
#                 res+=str[i]
#             else:
#                 res+=chr(ord(str[i])+32)
#         return res
    

# title = "Leetcode is cool"
# sol=Solution()
# print(sol.capitalizeTitle(title))



# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         new_word=""
#         new_sen=""
#         s= title
#         s= s + " "
#         i=0
#         while i < len(s):
#             if s[i]!=" "  :
#                 new_word= s[i] + new_word
            
#             elif new_word!="":

#                 if len(new_word)>=3:
#                     for i in range(len(new_word)):
#                         if new_word[i]==0:
#                             new_word[i].upper()
#                         else:
#                             new_word[i].lower()
                

                
#                 if new_sen!="":
#                     new_sen= new_sen + " " + new_word
#                 else:
#                     new_sen= new_sen+ new_word
#                 new_word=""
#             i+=1
#         return new_sen
    
# title = "Leetcode is cool"
# sol=Solution()
# print(sol.capitalizeTitle(title))




# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         new_word=""
#         new_sen=""
#         s= title
#         s= s + " "
#         i=0
#         while i < len(s):
#             if s[i]!=" "  :
#                 new_word= s[i] + new_word
            
#             elif new_word!="":
#                 if (capital(new_word)):
                
#                 if new_sen!="":
#                     new_sen= new_sen + " " + new_word
#                 else:
#                     new_sen= new_sen+ new_word
#                 new_word=""
#             i+=1
#         return new_sen











# WAP to replace a word in a giiven sentence.
# I/P:
# s1 = apples are blue roses are BLUE
# word to be replaced = blue
# new word = red

# O/P:
# apples are red roses are red



# s= input("ENter a string: ")

# def replace_word(s):
#     new_word=""
#     new_sen=""
#     s= s + " "
#     i=0
#     while i < len(s):
#         if ("A"<= s[i]<= "Z") or ("a"<= s[i]<= "z")  :
#             new_word= new_word+ s[i]
           
#         elif new_word!="":
#             if new_word=="blue" or new_word=="BLUE":
#                 new_word="red"
#             if new_sen!="":
#                 new_sen= new_sen + " " + new_word

#             else:
#                 new_sen= new_word
#             new_word=""
#         i+=1
#     return new_sen

# print(replace_word(s))









# Remove a word from the given sentence
# I/P:
# apples are blue roses are BLUE
# word to be removed = blue

# O/P:
# apples are roses are




s= input("ENter a string: ")

def replace_word(s):
    new_word=""
    new_sen=""
    s= s + " "
    i=0
    while i < len(s):
        if ("A"<= s[i]<= "Z") or ("a"<= s[i]<= "z")  :
            new_word= new_word+ s[i]
           
        elif new_word!="":
            if new_word=="blue" or new_word=="BLUE":
                new_word=""
            if new_sen!="":
                new_sen= new_sen + " " + new_word

            else:
                new_sen= new_word
            new_word=""
        i+=1
    return new_sen

print(replace_word(s))
