class Vehicle:
    def __init__(self, make, year, availability):
        self.make = make
        self.year = year
        self.availability = availability

class Car(Vehicle):
    def __init__(self, make, year, availability, body_type, number_of_doors):
        super().__init__(make, year, availability)
        self.body_type = body_type
        self.number_of_doors = number_of_doors
    @classmethod
    def from_string(cls, assemble):
            make, year, availability, body_type, number_of_doors = assemble.split(",")
            return cls(make.strip(), int(year), availability.strip() == "True", body_type.strip(), int(number_of_doors))
    
    @staticmethod
    def display_cars(cars):
        for car in cars:
            print(f"{car.year} {car.make} {car.body_type} with {car.number_of_doors} doors. Available: {car.availability}")

car1 = Car.from_string("Ford,2015,True,Truck,4")
car2 = Car.from_string("Kia,2018,False,sedan,4")
cars = [car1, car2]

while True:
    print("\nWelcome to the Boston Police Department\n")
    print("1. See a list of all cars.")
    print("2. See a list of all motorcycles.")
    print("3. Add a new vehicle.")
    print("4. See the count of every type of vehicle.")
    print("5. Exit")
    answer = input("\nPlease choose an option (1-5). ")

    if answer == '1':
        Car.display_cars(cars)
    elif answer == '5':
        print("Goodbye and have a nice day!")
        break
    else:
        print("Invalid input.")
