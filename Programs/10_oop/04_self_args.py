class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))  
# A 150ml chai cup
# A 150ml chai cup

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))
# A 100ml chai cup
