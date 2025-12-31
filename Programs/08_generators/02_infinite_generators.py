def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(next(refill))

# Refil #1
# Refil #2
# Refil #3    

for _ in range(6):
    print(next(user2))

# Refil #1
# Refil #2
# Refil #3
# Refil #4
# Refil #5
# Refil #6