
################### Pure function
# def pure_chai(cups):
#     return cups * 10

# total_chai = 0

#################### # Impure function
# # not recommended 
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups


#################### Recursive Function
# def pour_chai(n):
#     print(n)
#     if n == 0:
#         return "All cups poured"
#     return pour_chai(n-1)

# print(pour_chai(3))
# # 3
# # 2
# # 1
# # 0
# # All cups poured

##################### Lambda or Anonymous function
# chai_types = ["light", "kadak", "ginger", "kadak"]

# strong_chai = list(filter(lambda chai:chai == "kadak",chai_types))

# print(strong_chai)
# # ['kadak', 'kadak']


# chai_types = ["light", "kadak", "ginger", "kadak"]

# strong_chai = list(filter(lambda chai:chai != "kadak",chai_types))

# print(strong_chai)
# # ['light', 'ginger']

######################## Built-in python function
