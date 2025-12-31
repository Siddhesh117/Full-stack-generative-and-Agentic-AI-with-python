def make_chai():
    return "Here is your masala chai"
    # print("Here is your masala chai")

return_value = make_chai()

print(return_value)
# Here is your masala chai


def idle_chaiwala():
    pass

print(idle_chaiwala()) 
# None

def chai_report():
    return 100, 20, 10

sold, remaining, not_paid = chai_report()

print("Sold: ", sold)
print("Remaining: ", remaining)
print("Not paid: ",not_paid)

# Sold:  100
# Remaining:  20
# Not paid:  10