# class kavana:
#     def __init__(self, Title, author, rating):
#         self.kavana_Title = Title
#         self.kavana_author = author
#         self.kavana_rating = rating

#     def display(self):
#         print("------------------------------------------------------------------------------------------------------------")
#         print(f" The rating for the {self.kavana_Title} is {self.kavana_rating} written by {self.kavana_author}")

# print(" I am excited to know the rating of the my kavana's")
# title= input("Enter the Title of the kavana: ")
# author= input("Enter the Author name: ")
# rating= int(input("Enter the rating of the kavana: "))

# kavana1= kavana(title, author, rating)

# kavana1.display()
# print("------------------------------------------------------------------------------------------------------------")
# print(" Thanks for rating my kavana")





#integer to roman
# def int_rom(n):
#     dict={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
#     sum=""
#     for key,val in dict.items():
#         while n>=key:
#             sum+=val
#             n=n-key
#     print(sum)
# n=int(input())
# int_rom(n)



#roman to integer
def rom_int(n):
    dict={"M":1000,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500}
    prev=0
    curr=0
    total=0
    for i in range(len(n)):
        curr=dict[n[i]]
        if curr>prev:
            total=total+curr-2*(prev)
        else:
            total+=curr
        prev=curr
    print( total)
n=input()
rom_int(n)