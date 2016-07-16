'''
Once you have everything working, refactor your code to make it more modular. You should:

Create a file named bicycles.py that contains each of your classes.
Create a file named main.py that imports those classes, and uses them.
Run main.py and make sure your refactored code still works like it did before.
'''

import random
from bicycle import Bicycle, Bike_Shops, Customers

#Create a list of bikes
bikesinventory = [
    Bicycle("BMX", 25, 150)            , Bicycle("Electric bikes", 50 , 500) ,
    Bicycle("Folding bikes", 22 , 1000) , Bicycle("Tandem bikes", 27 , 600)   ,
    Bicycle("Classic bikes", 23 , 200) , Bicycle("Recumbent", 20 , 300)      ,
    ]

bikeshop = Bike_Shops("Speedy Bikes Shop", 15, bikesinventory)

print bikeshop

# Create a list of customer with the fund that they ave
customers = [Customers("Ken", 200), Customers("Paul", 500), Customers("Sue", 1000)]

for customer in customers:

    bikesinventory = ", ".join( bike.model for bike in bikeshop.selection(customer.fund) )
    print customer.name, "can buy", bikesinventory 
        
#print bikeshop
print ""
template = "{0} bought the {1} at ${2}, and has ${3} left over." 
for customer in customers:
    
    affordableprice = bikeshop.selection(customer.fund)
    bikeshop.sell(random.choice(affordableprice), customer)
    print template.format(customer.name ,customer.bike.model,customer.bike.price,customer.fund)  
    
print ""
print bikeshop    