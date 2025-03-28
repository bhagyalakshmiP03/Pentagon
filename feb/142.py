# #identity op
# a=10
# b=5*2
# c=15
# d=c
# print(a is b)
# print(b is not a )
# print(a is c)
# print(id(a and b))
# print(id(c and d))

# s1= "Bhagya.03"
# print("a" in s1)
# print("R" in s1)
# a=100
# # print(0 in a)  #TypeError: argument of type 'int' is not iterable
# print("a" in "s1") # act character as string within double quote



#Simple if
# B= "Single"
# if("S" in B):
#     print("u r single")
# print("life executed")


# #if-else
# n=int(input("Enter num:"))
# if n > 0:
#     print("Negative num")
# else:
#     print("Positive num")
# print("program exec")

status = input("Enter the WhatsApp status (online/offline): ").lower()

if status == "online":
    tick_status = input("Enter the tick status (double tick grey / double tick blue): ").lower()
    
    if tick_status == "double tick grey":
        print("They are ignoring your message.")
    elif tick_status == "double tick blue":
        print("They have seen your message.")
    else:
        print("Invalid tick status entered.")
        
elif status == "offline":
    tick_status = input("Enter the tick status (single tick): ").lower()
    
    if tick_status == "single tick":
        print("Message sent but not delivered.")
    else:
        print("Invalid tick status for offline mode.")
        
else:
    print("Invalid status entered.")
print("Thank you for using WhatsApp!")



cur_bal=int(input("enter the current balance :"))
withdrawl=int(input("enter the withdrawl amount :"))
if withdrawl<=cur_bal:
    print(f"""
              Transaction is processing..wait!!
              Transcation is completed
              Balance:Rs. {cur_bal-withdrawl}""")
else:
    print("Insufficient Funds")




print("enter the side of the triangle")
s1=int(input())
s2=int(input())
s3=int(input())
if s1==s2 and s2==s3 and s3==s1:
    print("it's an Equilateral triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("it's an Isosceles triangle")
else:
    print(" it's a Scalene triangle")




print("Select the destination")
des=int(input("""
          1.International
          2.Domestic
          choose 1 or 2 :
          """))
cla=int(input("""
          1.First Class
          2.Economy
          choose 1 or 2:
          """))
if des==1:
    if cla==1:
        print(" 15 % grand Discount offer on Booking Tickets")
    else:
        print(" 10 % Discount Offer on  Booking Tickets")
else:
    if cla==1:
        print(" 5 % Discount offer on Booking Tickets")
    else:
        print("Booking Ticket ")

print("kindly enter the loaction Type to estimate the delivery time!!")
loc=int(input("""
             1.Local
             2.Regional
             3.National
             4.International
             """))
if loc==1:
    print("It will take 1 day for delivery")
elif loc==2:
    print("It will take 2 days for delivery")
elif loc==3:
    print("It will tale 3 days for delivery")
else:
    print("Opps!! It will take 4 days for delivery ..stay Tuned!!")





print("Buy Your Tickets..!! ")
age = int(input("Enter the person's age: "))
group = input("Is the person in a group? (yes/no): ").lower()

if age < 12:  # Child
    if group == "yes":
        price = 0
        print("Ticket is free for children in a group.")
    else:
        price = 10
        print("Ticket price: $10")
elif age >= 12:  # Adult
    if group == "yes":
        price = 20 * 0.8  # 20% discount on $20
        print(f"Ticket price with group discount: ${price:.2f}")
    else:
        price = 20
        print("Ticket price: $20")
else:
    print("Invalid input.")

print("Enjoy your visit to the theme park!")