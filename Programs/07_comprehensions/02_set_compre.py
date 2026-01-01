

favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi"
]

unique_chai = {chai for chai in favourite_chais  }

print(unique_chai)
# {'Lemon Tea', 'Elaichi', 'Masala Chai', 'Green Tea'}

unique_chai = {chai for chai in favourite_chais if len(chai) > 8  }

print(unique_chai)
# {'Green Tea', 'Lemon Tea', 'Masala Chai'}

recipes = {
    "Masala Chai":["ginger", "cardamom", "clove"],
    "Elaichi Chai":["cardamom", "milk"],
    "Spicy Chai":["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values for spice in ingredients}

print(unique_spices)
# {'milk', 'ginger', 'clove', 'cardamom', 'black pepper'}