is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # upcasting
print(f"Total actions: {total_actions}") # 6   => (5 + 1) => 6

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}") # Is there milk? False

milk_present = 1 # no milk
print(f"Is there milk? {bool(milk_present)}") # Is there milk? True

milk_present = None
print(f"Is there milk? {bool(milk_present)}") # Is there milk? False

milk_present = "milk"
print(f"Is there milk? {bool(milk_present)}") # Is there milk? True

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}") # Can serve chai? False

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}") # Can serve chai? True