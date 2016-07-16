'''
create Bicycle, Bike Shops, and Cjustomers classes to represent each of the following parts of our model:

Bicycle
-Have a model name
-Have a weight
-Have a cost to produce
Bike Shops
-Have a name
-Have an inventory of different bicycles
-Sell bicycles with a margin over their cost
-Can see how much profit they have made from selling bikes
Customers
-Have a name
-Have a fund of money to buy a bike
-Can buy and own a new bicycle

The code should:

Create a bicycle shop that has 6 different bicycle models in stock. The shop should 
charge its customers 20% over the cost of the bikes.
Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
Print the name of each customer, and a list of the bikes offered by the bike shop that 
they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
Print the initial inventory of the bike shop for each bike it carries.
Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

Once you have everything working, refactor your code to make it more modular. You should:

Create a file named bicycles.py that contains each of your classes.
Create a file named main.py that imports those classes, and uses them.
Run main.py and make sure your refactored code still works like it did before.
'''

'''
Customers
-Have a name
-Have a fund of money to buy a bike
-Can buy and own a new bicycle
'''
class Customers():
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bike = None


'''
Bicycle
-Have a model name
-Have a weight
-Have a cost to produce
'''
class Bicycle():
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):
        #"{:<10s}{:>10d}".format(word, number)
        template = "{0}: Cost: ${1}, Weight: {2} lb"
        return template.format(self.model, self.cost, self.weight)
'''    
Bike Shops
-Have a name
-Have an inventory of different bicycles
-Sell bicycles with a margin over their cost
-Can see how much profit they have made from selling bikes    
'''    
class Bike_Shops():
    def __init__(self, shopname, margin, bikes):
        self.shopname = shopname
        self.margin = margin
        
        self.profit = 0
        self.inventory = {}
        
        for bike in bikes:
            bike.markup = int(bike.cost / 100.0) * self.margin
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike

    def __repr__(self):
        template = "\n{0} (${1} profit)\n{2}\n"
        bikes = "\n".join( str(bike) for bike in self.inventory.values() )
        return template.format(self.shopname, self.profit, bikes)    

    def selection(self, customer_fund): 
        '''
        for bike in self.inventory.values():
            if bike.price <= customer_fund:
                return [bike]
        '''    
        return [ bike for bike in self.inventory.values() if bike.price <= customer_fund ]
    

    #Sell bicycles with a margin over their cost
    def sell(self, bike, customer):
        customer.bike = bike
        customer.fund -= bike.price
        self.profit += bike.markup
        del self.inventory[bike.model]
        
            

    
