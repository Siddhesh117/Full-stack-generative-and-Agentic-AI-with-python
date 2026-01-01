
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for visiting chaicode!")


bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)                
# Error:  That chai is not available
# Thank you for visiting chaicode!
# Error:  Number of cups must be an integer
# Thank you for visiting chaicode!
# Your bill for 3 cups of ginger chai: rupees 120
# Thank you for visiting chaicode!