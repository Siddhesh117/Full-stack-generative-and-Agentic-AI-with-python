
class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)  # hot

cutting.temperature = "Mild"
print("After changing ",cutting.temperature)
print("Direct look into the class ", Chai.temperature)
# After changing  Mild
# Direct look into the class  hot

cutting.cup = "small"
print("cup size is ", cutting.cup) 
# cup size is  small

del cutting.temperature
print(cutting.temperature) # hot ( default value get from the class)

del cutting.cup
# print("cup size is ", cutting.cup) 
# AttributeError: 'Chai' object has no attribute 'cup'