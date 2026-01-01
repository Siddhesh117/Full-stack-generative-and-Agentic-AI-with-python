
def process_order(item, quantity):
    try:
        price = {"masala":20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not no menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)        
# Sorry that chai is not no menu        
process_order("masala", "two")  # Operator overloading
# Total cost is parameter is either empty or invalid.wotwotwotwotwotwotwotwotwo

