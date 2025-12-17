essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")
# All Spices: {'cinnamon', 'cardamom', 'ginger', 'cloves', 'black pepper'}

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")
# Common Spices: {'ginger'}

only_in_essential = essential_spices - optional_spices
print(f"Only in essential: {only_in_essential}")
# Only in essential: {'cinnamon', 'cardamom'}

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices} ")
# Is 'cloves' in optional spices? True
