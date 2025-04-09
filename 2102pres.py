class Product:
    def __init__(self,pid,pname,price):
        self.productname=pname
        self.productid=pid
        self.product_price=price
        self.discount=0
    def display(self):
        
        print(f"ID: {self.productid}")
        print(f"Name: {self.productname}")
        print(f"Price: {self.product_price}")

    def applyDiscount(self,percentage):
        if self.product_price >= 1000 and percentage <= 50:
            self.discount=float(self.product_price) *(percentage/100)
            print(f"the discounted price of {self.productname} is {self.discount}")
        elif self.product_price >= 500 and percentage <= 30:
            self.discount=float(self.product_price) *(percentage/100)
            print(f"the discounted price of {self.productname} is {self.discount}")
        else:
            print(f" for the price {self.product_price}, {percentage}% of discount is not available")

print(f"Enter the details of product,")
name=input("Name: ")
id=input("Id: ")
price=int(input("Price: "))
obj=Product(id,name,price)

obj.display()
if obj.product_price < 500:
    print("for this price we dont provide any discounts")
else:
    discount=int(input("enter the rate of dicount: "))
    obj.applyDiscount(discount)
print("---------------------------------------------------------------")

























# print(" the product details are as follows")
# for obj in lst:
#     print(f"details of product {lst.index(obj)+1}")
#     obj.display()
#     discount=int(input("enter the rate of dicount: "))
#     obj.applyDiscount(discount)
#     print("---------------------------------------------------------------")

    

    
    



    


