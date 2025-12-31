def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # nonlocal chai_type   # refer just outside function  not out side like global
        chai_type = "Keser"
    kitchen()
    print("After kitchen update", chai_type)    

update_order()    

# After kitchen update Keser

# If comment    # nonlocal chai_type then 
# After kitchen update Elaichi


