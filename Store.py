Product.py 

#Product class with private classes including the set and get methods


#constructor with private methods of the product
class Product:
    def _init_(self, id_code, title, description, price, quantity_available):
        self._id_code =id_code
        self._title =title
        self._description =description
        self._price =price
        self._quantity_available =quantity_available


#get methods to retreive information from the private methods above

    #get id_code with a return value of the idcode
    def get_id_code(self):
        return self._id_code

    #get title with a return value of the title
    def get_title(self):
        return self._title

    #get description with return value of description
    def get_description(self):
        return self._description

    #get price, with a return value of the price
    def get_price(self):
        return self._price

    #get quantity with the return value of the quantity available
    def get_quantity_available(self):
        return self._quantity_available

    #decrease the quantity minus the quantity available from above by 1
    def decrease_quantity(self):
        return self._quantity_available - 1

Customer.py

#Customer class with private classes including the set and get methods


#constructor with private methods of the customer class

class Customer:
    def _init_(self, name, account_id, premium_member):
        self._name =name
        self._account_id=account_id
        self._premium_member =premium_member
        self._cart = []

    # get name with a return value of the name
    def get_name(self):
        return self._name

    # get account_id with a return value of the account_id
    def get_account_id(self):
        return self._account_id

    # return to see if the customer name is a premium member. In order to do this
    # you will need to use a simple if statement. If the name is a premium member then
    # it will return true but if not then it will return a value of false.
    def premium_member(self):
        if self.premium_member:
            return True
        else:
            return False

    # need to add product to cart with the use of id code to this file
    def add_product_to_cart(self, id_code):
        return self._cart.append(id_code)

    # empty cart from the customer
    def empty_cart(self):
        self._cart = []

Store.py

#Store class with private classes including the set and get methods and if statements

#constructor with private methods of the store class
class Store:
    def __init__(self):
        self._inventory = []
        self._members = []

# add product to the inventory
    def add_product(self, product):
        self._inventory.append(product)

#add member to members
    def add_member(self, member):
        self._members.append(member)

#return a product with a matching and nonmatching ID
    def get_product_from_ID(self, product_ID ):
        for product in self._inventory:
            if product_ID == product.get._id_code():
                return product
            else:
                return None

#return customer with either a matching or nonmatching ID
    def get_member_from_ID(self, customer_ID ):
        for customer in self._members:
            if customer_ID == customer.get._account_id():
                return customer
            else:
                return None

#searches and returns a sorted list of ID codes
    def product_search(self, search_string):
        for product in self._inventory:
            if (search_string, product.get_title()) or (search_string, product.get_description()):
                self._search_string.append(product.get._id_code)
                return self.sort()

#if a product is not found, returns a product not found explaination
    def add_product_to_member_cart(self, customer_ID, product_ID):
        for product in self.inventory:
            if product.get_id_code()== product_ID:
                for customer in self._members:
                    if customer.get_account_id()== customer_ID:
                        if product.get_quantity_available > 0:
                            customer.add_product_to_cart(product)
                            print("Product has been added to your cart")
                        else:
                            print("The product cannot be added to your cart.")

#total cost of all items in the cart of an member
    def check_out_member(self, _premium_member):
        total = 0.00
        for customer in self._members:
           if(customer.is_premium_member()):
            return (total *7 /100)
        else:
            return total



StoreTester.py
#testing 
#1.
from Customer import Customer
from Product import Product
from Store import Store

p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
c1 = Customer("Yinsheng", "QWF", False)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product_to_member_cart("889", "QWF")
result = myStore.check_out_member("QWF")

#2.
p1 = Product("32", "snow falls at", "particular temperature", 32, 10)
c1 = Customer("Neha", "ASA", True)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product_to_member_cart("32", "ASA")
result = myStore.check_out_member("ASA")



#3.
p1 = Product("9", "The grade you join", "high school is 9", 9, 8)
c1 = Customer("Freshman", "BBB", False)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product_to_member_cart("9", "BBB")
result = myStore.check_out_member("BBB")


#4.
p1 = Product("20", "The price of any inexpensive", "jacket", 20, 10)
c1 = Customer("Eddie Bauer", "EEB", True)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product_to_member_cart("20", "EEB")
result = myStore.check_out_member("EEB")

#5.
p1 = Product("999", "Price of an laptop", "is roughly 900 for Apple", 999, 900)
c1 = Customer("Apple", "AAA", False)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product_to_member_cart("999", "AAA")
result = myStore.check_out_member("AAA")























