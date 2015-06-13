'''
Product Inventory Project - 
Create an application which manages an inventory of products. Create a product 
class which has a price, id, and quantity on hand. Then create an inventory 
class which keeps track of various products and can sum up the inventory value.
'''

#------------------------------------------------------------------------------
# PRODUCT class definition
#------------------------------------------------------------------------------
class Product(object):
    # productId class variable, updated after the creation of a new product
    # This enforces unique, integer product IDs 
    productID = 0

    # Initialize product with non-negative price
    # Keep track of quantity in inventory only
    def __init__(self, name, price):
        if price < 0:
            raise ValueError('Price cannot be negative')
        self.name = name
        self.price = price
        self.pID = Product.productID
        # Note: This is not thread-safe
        Product.productID += 1

    # Change product price
    def updatePrice(self, price):
        if price < 0:
            raise ValueError('Price cannot be negative')
        self.price = price

    def __repr__(self):
        return "ProductName = %s, ProductID : %d, Price : %f" \
                % (self.name, self.pID, self.price)

#------------------------------------------------------------------------------
# INVENTORY class definition
#------------------------------------------------------------------------------
class Inventory(object):
    def __init__(self):
        # Keep track of products and their quantities
        self.inventory = {}
    
    # Add product to inventory
    def addProduct(self, product, quantity = 1):
        self.inventory[product] = self.inventory.get(product, 0) + quantity

    # Remove product from inventory
    def removeProduct(self, product, removeAll = True, quantity = 1):
        # If removeAll is False, then this method removes #quantity 
        # items of product, else it removes all items of product
        if self.inventory.get(product, None) == None:
            print "Product " + product.name + " doesn't exist in inventory"
        else:
            if removeAll:
                print "Removing " + product.name + " entirely from inventory"
                self.inventory.pop(product, None)
            else:
                if quantity < self.inventory[product]:
                    self.inventory[product] -= quantity
                else:
                    print "Removing " + product.name + " entirely from inventory"
                    self.inventory.pop(product, None)
   
    # Inventory value = total price of items in inventory
    def getInventoryValue(self):
        value = 0
        for product in self.inventory.keys():
            value += product.price * self.inventory[product]
        return value
   
    def __repr__(self):
        value = self.getInventoryValue()
        inventory_string = "Name ProductID Price Quantity\n"
        for product in self.inventory.keys():
            inventory_string += str(product.name) + "\t" + str(product.pID) \
                                + "\t" + str(product.price) + "\t"\
                                + str(self.inventory[product]) + "\n"
        inventory_string += "Total value = " + str(value)
        return inventory_string


# Do some tests
if __name__ == "__main__":
    plate = Product("Plate", 8.5)
    spoon = Product("Spoon", 2.0)
    fork = Product("Fork", 2.0)
    bowl = Product("Bowl", 9.0)
    napkin = Product("Napkin", 1.5)

    print "Products created:"
    print plate
    print spoon
    print fork
    print bowl
    print napkin

    inv = Inventory()
    inv.addProduct(plate, 2)
    inv.addProduct(spoon, 2)
    inv.addProduct(fork, 2)
    inv.addProduct(bowl, 1)
    inv.addProduct(napkin, 4)

    print "Inventory:"
    print inv

    # Update price of bowl
    bowl.updatePrice(7.0)
    print bowl

    print "Inventory:"
    print inv

    # Remove 2 napkins
    inv.removeProduct(napkin, False, 2)

    print "Inventory:"
    print inv
