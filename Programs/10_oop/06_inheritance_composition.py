

class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

# This is Inherit of base class
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, clover.")



class ChaiShop:
    # This is Reference of class
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")                 
        self.chai.prepare()


# This is Inherit of base class
class FancyChaiShop(ChaiShop):

    # This is Reference of class
    # Compositing
    chai_cls = MasalaChai



shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()




# What is Inheritance (Is-A Relation)? 
# It is a concept of Object-Oriented Programming. Inheritance is a mechanism that allows us 
# to inherit all the properties from another class. The class from which the properties and 
# functionalities are utilized is called the parent class (also called as Base Class).
#  The class which uses the properties from another class is called as Child Class
#     (also known as Derived class). Inheritance is also called an Is-A Relation. 

# # parent class
# class Parent:

#     # parent class method
#     def m1(self):
#         print('Parent Class Method called...')

# # child class inheriting parent class
# class Child(Parent):

#     # child class constructor
#     def __init__(self):
#         print('Child Class object created...')

#     # child class method
#     def m2(self):
#         print('Child Class Method called...')


# # creating object of child class
# obj = Child()

# # calling parent class m1() method
# obj.m1()

# # calling child class m2() method
# obj.m2()


# What is Composition (Has-A Relation)? 
# It is one of the fundamental concepts of Object-Oriented 
# Programming. In this concept, we will describe a class that references to one or more 
# objects of other classes as an Instance variable. Here, by using the class name or by 
# creating the object we can access the members of one class inside another class. 
# It enables creating complex types by combining objects of different classes. 
# It means that a class Composite can contain an object of another class Component. 
# This type of relationship is known as Has-A Relation.

# class Component:

#    # composite class constructor
#     def __init__(self):
#         print('Component class object created...')

#     # composite class instance method
#     def m1(self):
#         print('Component class m1() method executed...')


# class Composite:

#     # composite class constructor
#     def __init__(self):

#         # creating object of component class
#         self.obj1 = Component()
        
#         print('Composite class object also created...')

#      # composite class instance method
#     def m2(self):
      
#         print('Composite class m2() method executed...')

#         # calling m1() method of component class
#         self.obj1.m1()


# # creating object of composite class
# obj2 = Composite()

# # calling m2() method of composite class
# obj2.m2()