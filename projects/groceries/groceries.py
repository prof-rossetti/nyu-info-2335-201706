import code
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

##CHECKPOINT 1

#1. Print the number of products.
print("--------------")
print("There are ".upper()+str(len(products))+" items:".upper())
#2. Print the name of each product.

#for product in products:
#    print(product["name"])

#3. Print in alphabetical order the name of each product.

def sort_by_product_name(product):
    return product['name']

products = sorted(products, key=sort_by_product_name)

#4. Print in alphabetical order the name of each product, and include its price rounded to two decimal places.

for product in products:
    print("+", product["name"].strip(), '(${0:.2f})'.format(product["price"], 2))


##CHECKPOINT 2
print("--------------")
#5. Print the number of unique departments.
dpmnts=[]
for x in range(len(products)):
    dpmnts.append(products[x]['department'])

print("There are ".upper()+str(len(set(dpmnts)))+" departments: ".upper())

#6. Print the name of each unique department.
dpmnts=list(set(dpmnts))

#for dpmnt in dpmnts:
#    print(dpmnt)

#7. Print in alphabetical order the name of each unique department.
dpmnts=sorted(dpmnts)
#for dpmnt in dpmnts:
#    print(dpmnt)

#8. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department.
depts_list = []

for product in products:
    depts_list.append(product["department"])

for dpmnt in dpmnts:
    print("+ " + dpmnt.title() + " (" + str(depts_list.count(dpmnt)) + " products)")

#print(depts_list)
#code.interact(local=locals())
