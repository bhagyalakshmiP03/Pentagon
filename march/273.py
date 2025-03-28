# # def filtration(s):
# #     new_str=""
# #     for i in range(len(s)):
# #         if "A"<= s[i]<= "Z":
# #             new_str+= chr(ord(s[i])+32)   #converting into smaller 
# #         elif ("a"<= s[i]<= "z") or ("0"<= s[i] <="9" ):
# #             new_str+= s[i]

# #     return new_str

# # def isPalindrome(s):
# #     s= filtration(s)
# #     i, j= 0, len(s)-1
# #     while i<= j:
# #         if s[i]!= s[j]:
# #             return False
# #         i+=1
# #         j-=1
# #     return True

# # s=input("Enter a string: ")

# # flag= isPalindrome(s)
# # if flag:
# #     print(s, " :is palindrome string")
# # else:
# #     print(s, " :is not palindrome string")








# ##PANGRAM
# # s= input("ENter a string: ")
# # def filtration(s):
# #     new_str=""
# #     for i in range(len(s)):
# #         if "A"<= s[i]<= "Z":
# #             new_str+= chr(ord(s[i])+32)   #converting into smaller 
# #         elif ("a"<= s[i]<= "z"):
# #             new_str+= s[i]
# #     return new_str

# # def pangram(s):
# #     s= filtration(s)
# #     if len(s)< 26:
# #         return False
    
# #     ascii= [0] * 26

# #     for i in range(len(s)):
# #         ascii[ord(s[i])-97] += 1

# #     if 0 in ascii:
# #         return False
# #     return True

# # flag= pangram(s)
# # if flag:
# #     print(s, " :is PANGRAM")   
# # else:
# #     print(s, ": is not PANGRAM")      



# ##ANAGRAM by +1 -1
# # s1= input("ENter a string1: ")
# # s2= input("Enter string 2: ")
# # def filtration(s):
# #     new_str=""
# #     for i in range(len(s)):
# #         if "A"<= s[i]<= "Z":
# #             new_str+= chr(ord(s[i])+32)   #converting into smaller 
# #         elif ("a"<= s[i]<= "z"):
# #             new_str+= s[i]
# #     return new_str


# # def angram(s1, s2):
# #     s1= filtration(s1)
# #     s2= filtration(s2)
# #     if len(s1)!= len(s2):
# #         return False
    
# #     ascii= [0] * 26

# #     for i in range(len(s1)):
# #         ascii[ord(s1[i])-97] += 1
# #         ascii[ord(s2[i])-97] -= 1

# #     for i in range(len(ascii)):
# #         if ascii[i]!=0:
# #             return False
# #     return True


# # flag= angram(s1, s2)
# # if flag:
# #     print(s1 , " ", s2, " :are ANGRAM")   
# # else:
# #     print(s1, " ", s2 , " : are not ANGRAM")    








# ## anagram by even
# s1= input("ENter a string1: ")
# s2= input("Enter string 2: ")
# def filtration(s):
#     new_str=""
#     for i in range(len(s)):
#         if "A"<= s[i]<= "Z":
#             new_str+= chr(ord(s[i])+32)   #converting into smaller 
#         elif ("a"<= s[i]<= "z"):
#             new_str+= s[i]
#     return new_str


# def angram(s1, s2):
#     s1= filtration(s1)
#     s2= filtration(s2)
#     if len(s1)!= len(s2):
#         return False
    
#     ascii= [0] * 26

#     for i in range(len(s1)):
#         ascii[ord(s1[i])-97] += 1
#         ascii[ord(s2[i])-97] += 1

#     for i in range(len(ascii)):
#         if ascii[i]%2 !=0:
#             return False
#     return True


# flag= angram(s1, s2)
# if flag:
#     print(s1 , " ", s2, " :are ANGRAM")   
# else:
#     print(s1, " ", s2 , " : are not ANGRAM")    






# 1. WAP to display all the palindromic words 
# in a given sentence.

# 	I/P:
# 		Madam Mrs. Lee teaches malayalam	
# 	O/P:
# 		Madam malayalam


# s= input("Enter a string: ")
# def filtration(s):
#     new_str=""
#     for i in range(len(s)):
#         if "A"<= s[i]<= "Z":
#             new_str+= chr(ord(s[i])+32)   #converting into smaller or lower case
#         elif ("a"<= s[i]<= "z")or s[i]==" ":
#             new_str+= s[i]
#     return new_str


# def allpalindromic(s):
#     s= filtration(s)
#     nw, ns= "", ""
#     s= s+ " "
#     for i in range(len(s)):
#         if s[i]!=" ":
#             nw+= s[i]
#         elif nw!="":
#             if palinrome(nw)== True:
#                 if ns!="":
#                     ns+= " " + nw
#                 else:
#                     ns= nw
#             nw= ""
#     return ns


# def palindrome(nw):
#     i, j= 0,len(nw)-1
#     while i<= j:
#         if nw[i]!= nw[j]:
#             return False
#         i+=1
#         j-=1
#     return True

# print(allpalindromic(s))






# 2. WAP to display the longest palindromic word 
# in a given sentence with their length.
   
# 	I/P:
# 		Madam Mrs. Lee teaches malayalam
# 	O/P:
# 		malayalam 9



# s= input("Enter a string: ")
# def filtration(s):
#     new_str=""
#     for i in range(len(s)):
#         if "A"<= s[i]<= "Z":
#             new_str+= chr(ord(s[i])+32)   #converting into smaller or lower case
#         elif ("a"<= s[i]<= "z")or s[i]==" ":
#             new_str+= s[i]
#     return new_str

# def palindrome(nw):
#     i, j= 0,len(nw)-1
#     while i<= j:
#         if nw[i]!= nw[j]:
#             return False
#         i+=1
#         j-=1
#     return True


# def allPalindromes(s):
#     s= filtration(s)
#     nw, ns= "", ""
#     s= s+ " "
#     for i in range(len(s)):
#         if s[i]!=" ":
#             nw+= s[i]
#         elif nw!="":
#             if palindrome(nw)== True:
#                 if ns!="":
#                     ns+= " " + nw
#                 else:
#                     ns= nw
#             nw= ""
#     return ns
# print(allPalindromes(s))
# def longest_palindrome(ns):
#     ns= ns+" "
#     nw, max_len= "", -2147383648
#     max_word= "" 
#     for i in range(len(ns)):
#         if ns[i]!=" ":
#             nw+= ns[i]
#         elif nw!="":
#             if len(nw)> max_len:
#                 max_len= len(nw)
#                 max_word= nw
#             nw= ""
#     return max_word, max_len

# print(longest_palindrome(allPalindromes(s)))





# 3. WAP to display the shortest palindromic word in 
# a given sentence with their length.
   
# 	I/P:
# 		Madam Mrs. Lee teaches malayalam
		
# 	O/P:
# 		Madam 5
	


# s= input("Enter a string: ")
# def filtration(s):
#     new_str=""
#     for i in range(len(s)):
#         if "A"<= s[i]<= "Z":
#             new_str+= chr(ord(s[i])+32)   #converting into smaller or lower case
#         elif ("a"<= s[i]<= "z")or s[i]==" ":
#             new_str+= s[i]
#     return new_str

# def palindrome(nw):
#     i, j= 0,len(nw)-1
#     while i<= j:
#         if nw[i]!= nw[j]:
#             return False
#         i+=1
#         j-=1
#     return True


# def allPalindromes(s):
#     s= filtration(s)
#     nw, ns= "", ""
#     s= s+ " "
#     for i in range(len(s)):
#         if s[i]!=" ":
#             nw+= s[i]
#         elif nw!="":
#             if palindrome(nw)== True:
#                 if ns!="":
#                     ns+= " " + nw
#                 else:
#                     ns= nw
#             nw= ""
#     return ns

# def longest_palindrome(s):
#     ns=allPalindromes(s)
#     ns= ns+" "
#     nw, min_len= "", 2147383648
#     min_word= "" 
#     for i in range(len(ns)):
#         if ns[i]!=" ":
#             nw+= ns[i]
#         elif nw!="":
#             if len(nw)< min_len:
#                 min_len= len(nw)
#                 min_word= nw
#             nw= ""
#     return min_word, min_len

# print(longest_palindrome(allPalindromes(s)))





# 4. WAP to count the highest number of continuous 
# palindromic words available in a given sentence
	
# 	I/P:
# 		madam malayalam wow are adjective words 
# 		malayalam kannada madam malayalam
		
# 	O/P:
# 		3





# 5. WAP to display the count of occurences of each
# character in a given string(without using 
# dictionary)
# s= input("Enter a string: ")
# def occurances(s):
#     ascii= [0]* 26
#     for i in s:
#         if "A"<= i<= "Z":
#             ascii[ord(i)-65]+=1
#         elif "a"<= i<= "z":
#             ascii[ord(i)-97]+=1
#     return ascii


# print(occurances(s))





#converting to dictonary
