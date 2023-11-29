from tabnanny import check


class Agent ():
    def __init__(self):
        self.property_list = []

    def add_property(self, property_type, purchase_type):
        self.property_type = property_type
        self.purchaser_type = purchase_type
        type_map = {("House", "Rental"): HouseRental,
                    ("House", "Purchase"): HousePurchase,
                    ("Apartment", "Rental"): ApartmentRental,
                    ("Apartment", "Purchase"): ApartmentPurchase}
        property_add = type_map.get((property_type, purchase_type))
        property_class = property_add.prompt_init()
        self.property_list.append(property_add(**property_class))

    def list_properties(self, show_all=False, id=None):
        if show_all == True:
            for i in self.property_list:
                print("="*30)
                i.display()
                print("="*30)
        else:
            print("\tSearch")
            for search in self.property_list:
                if (search.id == id):
                    print("="*30)
                    search.display()
                    print("="*30)


class Property ():
    _idnum = 0

    def __init__(self, square_feet=0, num_bedrooms=0, num_bathrooms=0, **kwargs):
        self._id = Property._idnum
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        Property._idnum = + 1

    @staticmethod
    def prompt_init():
        id = Property._idnum
        propertydict = {}
        square_feet = int(input("Please Enter Square Feet : "))
        num_bedrooms = int(input("Please Enter Num of Bedrooms : "))
        num_bathrooms = int(input("Please Enter Num of Bathroom : "))
        propertydict = {"id": id, "square_feet": square_feet,
                        "num_bedrooms": num_bedrooms, "num_bathrooms": num_bathrooms}
        return propertydict

    def display(self):
        print("ID : ", self._idnum)
        print("Square Feet : ", self.square_feet)
        print("Num of bedrooms : ", self.num_bedrooms)
        print("Num of Bathrooms : ", self.num_bathrooms)

    @property
    def id(self):
        return self._idnum


class House (Property):
    def __init__(self, garage='', fenced_yard='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced_yard = fenced_yard

    @staticmethod
    def prompt_init():
        housedict = {}
        prom = Property.prompt_init()
        garage = int(input("Do you have How Many Garage Space : "))
        check = True
        while check:
            fenced_yard = input("Do you have Fenced yard y/n : ").upper()
            if fenced_yard == "Y" or fenced_yard == "N":
                housedict = {"garage": garage, "fenced_yard": fenced_yard}
                return housedict | prom
                break
            else:
                print("Please Enter Y or N")

    def display(self):
        super().display()
        print("Garage : ", self.garage)
        print("Fenced Yard : ", self.fenced_yard)


class Apartment (Property):
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    @staticmethod
    def prompt_init():
        apartmentdict = {}
        prom = Property.prompt_init()
        check = True
        while check:
            balcony = input("Do you have Balcony y/n : ").upper()
            if balcony == "Y" or balcony == "N":
                while True:
                    laundry = input("Do you have Laundry y/n : ").upper()
                    if laundry == "Y" or laundry == "N":
                        apartmentdict = {
                            "balcony": balcony, "laundry": laundry}
                        return apartmentdict | prom
                        break
                    else:
                        print("Please Enter Y or N")
            else:
                print("Please Enter Y or N")

    def display(self):
        super().display()
        print("Balcony : ", self.balcony)
        print("Laundry : ", self.laundry)


class Purchase ():
    def __init__(self, price=0, **kwargs):
        self.price = price

    @staticmethod
    def prompt_init():
        pricedict = {}
        price = int(input("What A Price :  "))
        pricedict = {"price": price}
        return pricedict

    def display(self):
        print("Price : ", self.price)


class Rental ():
    def __init__(self, funisched, rent, **kwargs):
        self.funisched = funisched
        self.rent = rent

    @staticmethod
    def prompt_init():
        rentaldict = {}
        while True:
            funisched = input("Do you need funisched y/n : ").upper()
            if funisched == "Y" or funisched == "N":
                rent = int(input("Rent : "))
                rentaldict = {"funisched": funisched, "rent": rent}
                return rentaldict
                break
            else:
                print("Please Enter Y or N")

    def display(self):
        print("Funisched : ", self.funisched)
        print("Rent : ", self.rent)


class HouseRental (House, Rental):
    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    def display(self):
        House.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        return House.prompt_init() | Rental.prompt_init()


class HousePurchase (House, Purchase):
    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    def display(self):
        House.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        return House.prompt_init() | Purchase.prompt_init()


class ApartmentPurchase (Apartment, Purchase):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    def display(self):
        Apartment.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        return Apartment.prompt_init() | Purchase.prompt_init()


class ApartmentRental (Apartment, Rental):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    def display(self):
        Apartment.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        return Apartment.prompt_init() | Rental.prompt_init()


A = Agent()
A.add_property("Apartment", "Rental")
# A.add_property("House","Purchase")
A.list_properties(True)

# B = Agent ()
# B.add_property("Apartment","Rental")
# B.list_properties(True)


A.list_properties(id=1)
