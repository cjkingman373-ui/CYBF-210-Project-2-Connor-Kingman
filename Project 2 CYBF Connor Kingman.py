#Project 2 by Connor Kingman

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

    @classmethod       #Used split to get single string seperated by commas
    def from_string(cls, assemble):
            make, year, availability, body_type, number_of_doors = assemble.split(",")
            return cls(make.strip(), int(year), availability.strip() == "True", body_type.strip(), int(number_of_doors))
   
    @staticmethod
    def display_cars(cars):   #Used for to take my car list and print out the car info since I would need to add cars later on and couldnt use [0], [1], etc
        for car in cars:
            print(f"{car.year} {car.make} {car.body_type} with {car.number_of_doors} doors. Available: {car.availability}")

car1 = Car.from_string("Ford,2015,True,Truck,4")
car2 = Car.from_string("Kia,2018,False,sedan,4")
cars = [car1, car2]

class Motorcycle(Vehicle):  #Set up subclass
    def __init__(self, make, year, availability, has_sidecar):
        super().__init__(make, year, availability)
        self.has_sidecar = has_sidecar

    @classmethod
    def from_string(cls, assemble):   #Used split to get a single string seperated by commas
        make, year, availability, has_sidecar = assemble.split(",")
        return cls(make.strip(), int(year), availability.strip() == "True", has_sidecar.strip() == "True")

    @staticmethod
    def display_motorcycles(motorcycles):    #Used for to seperate the two scenarios im checking for (side car or no side car)
        for bike in motorcycles:
            if bike.has_sidecar:
                print(f"{bike.year} {bike.make} motorcycle with a sidecar. Available: {bike.availability}. ")
            else:
                print(f"{bike.year} {bike.make} motorcycle WITHOUT a sidecar. Available: {bike.availability}.")

motorcycle1 = Motorcycle.from_string("Yamaha,2024,True,False")
motorcycle2 = Motorcycle.from_string("Harley-Davidson,2025,False,True")
motorcycles = [motorcycle1, motorcycle2]

while True: #Setting up the menu, I wanted to try using a different method I saw you use in class as a demonstration but stuck with what I knew off the head
    print("\nWelcome to the Boston Police Department\n")
    print("1. See a list of all cars.")
    print("2. See a list of all motorcycles.")
    print("3. Add a new vehicle.")
    print("4. See the count of every type of vehicle.")
    print("5. Exit")
    answer = input("\nPlease choose an option (1-5).")
    print() #Just for the menu don't worry about this

    if answer == '1':
        Car.display_cars(cars)
    elif answer == '2':
        Motorcycle.display_motorcycles(motorcycles)
    elif answer == '3':
        build = input("Enter 1 to add a new car or enter 2 to add a new motorcycle.")
        if build == '1':
            new_car_info = input("Please enter the details of the car as shown, (make,year,availability(True/False),body_type,number_of_doors).")
            try:  #I chose to use try and except here because my build == 2 wasn't getting checked by just else
                new_car = Car.from_string(new_car_info)
                cars.append(new_car)
                print("Your car has been successfully added.")
            except:
                print("An error occurred adding your car, please try again.")
        elif build == '2':
            new_motorcycle_info = input("Please enter the details of the motorcycle as shown, (make,year,availability(True/False),has_sidecar)")
            try:
                new_motorcycle = Motorcycle.from_string(new_motorcycle_info)
                motorcycles.append(new_motorcycle)
                print("Your motorcycle has been successfully added.")
            except:
                print("An error occurred adding your motorcycle, please try again.")
        else:
            print("Invalid option.")
    elif answer == '4':   #Straightforward, just taking my already existing lists and taking the lengths of them and combining for total vehicles
        total_cars = len(cars)
        total_motorcycles = len(motorcycles)
        total_vehicles = total_cars + total_motorcycles
        print(f"There are {total_vehicles} vehicles in total: {total_cars} are cars and {total_motorcycles} are motorcycles.")
    elif answer == '5':
        print("Goodbye and have a nice day!\n")
        break
    else:
        print("Invalid input.")

#Everything ran correctly for me but I'm sure there are parts that could be simplified or improved.