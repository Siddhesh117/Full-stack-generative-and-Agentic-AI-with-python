chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")
# Chai order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
# Recipe base: black tea

print(f"Recipe: {chai_recipe}")
# Recipe: {'base': 'black tea', 'liquid': 'milk'}

del chai_recipe["liquid"]

print(f"Recipe: {chai_recipe}")
# Recipe: {'base': 'black tea'}

print(f"Is sugar in the order? {'sugar' in chai_order}")
# Is sugar in the order? True

chai_order = {"type":"Ginger Chai", "size":"Medium", "Sugar":1}

# print(f"Order details (keys): {chai_order.keys()}")
# Order details (keys): dict_keys(['type', 'size', 'Sugar'])

# print(f"Order details (values): {chai_order.values()}")
# Order details (values): dict_values(['Ginger Chai', 'Medium', 1])

# print(f"Order details (items): {chai_order.items()}")
# Order details (items): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('Sugar', 1)])

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")
# Removed last item: ('Sugar', 1)

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")
# Updated chai recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

chai_size = chai_order['size']
print(f"Chai size is: {chai_size}")
# Chai size is: Medium

# Safely get property if not available add default value
customer_note = chai_order.get("note","No note")
print(f"Customer note is: {customer_note}")
# Customer note is: No note
