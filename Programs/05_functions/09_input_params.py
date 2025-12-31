


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keywords

# Darjeeling Yes Low
# Green No Medium

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardamom", sweeter="Honey", foam="yes")    

# Ingredients ('Cinnamon', 'Cardamom')
# Extras {'sweeter': 'Honey', 'foam': 'yes'}


# def chai_orders(order=[]):
#     order.append("Masala")
#     print(order)

# chai_orders()    
# chai_orders()    

# ['Masala']
# ['Masala', 'Masala']

def chai_orders(order=None):
    if order is None:
        order = []
    print(order)    

chai_orders()   