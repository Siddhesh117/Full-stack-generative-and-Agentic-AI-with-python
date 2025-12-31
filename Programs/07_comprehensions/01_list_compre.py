

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)
# ['Iced Lemon Tea', 'Iced Peach Tea']

iced_tea = [my_tea for my_tea in menu if "Iced" if len(my_tea) < 12]

print(iced_tea)
# ['Masala Chai', 'Green Tea', 'Ginger chai']