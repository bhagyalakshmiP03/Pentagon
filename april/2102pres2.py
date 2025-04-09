class Car:
    def __init__(self,model,price):
        self.carmodel=model
        self.rentprice=price
        self.isAvailable=False
    def rentCar(self):
        print("handle the vehicle with care")
        self.isAvailable=False
        
    def returnCar(self):
        print("Thanks for returning the car, visit us again")
        self.isAvailable=True
        

print("Enter the details of car: ")
model=input("Model: ")
rentprice=input("Price: ")
car1=Car(model,rentprice)
# print("Car details are as follows: ")
# print(f"Model: {car1.carmodel}")
# print(f"rentalprice: {car1.rentprice}")
while True:
    print("enter the option, what do you want rent or return the car")
    print("1-> to rent a car")
    print("2-> to return a car")
    print("3-> to exit")
    choice=int(input())
    if choice == 1:
        if car1.isAvailable:
            print(f"model: {car1.carmodel}")
            print(f"rental price: {car1.rentprice}")
            print("its available for rent")
            print("do you want to take it(yes/no)")
            decision=input()
            if decision == 'yes':
                car1.rentCar()
            else:
                print("thank you visit us again")
        else:
            print(f"model: {car1.carmodel}")
            print(f"rental price: {car1.rentprice}")
            print("sorry this car is not available for rent now")
    elif choice == 2:
        car1.returnCar()
    elif choice == 3:
        break
    else:
        print("please enter a proper choice")
            



