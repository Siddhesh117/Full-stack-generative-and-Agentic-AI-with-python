

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

# Cup 1: Masala Chai
# Cup 2: Ginger Chai
# Cup 3: Elaichi Chai

# Normal Function
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator Function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
# print(chai)
# <generator object get_chai_gen at 0x000001FDE6935C70>

# print(next(chai))
# # Cup 1
# print(next(chai))
# # Cup 2
# print(next(chai))
# # Cup 3
# print(next(chai))
# Traceback (most recent call last):
#   File "C:\Users\a2z\Documents\python-fullstack-ai\Programs\08_generators\01_basics.py", line 37, in <module>
#     print(next(chai))
# StopIteration