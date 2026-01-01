
# Global Interpreter Lock (GIL)

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range (100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")    
thread2 = threading.Thread(target=brew_chai, name="Barista-2")    

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken:{end - start:.2f} seconds")


# Barista-1 started brewing...
# Barista-2 started brewing...
# Barista-1 finished brewing...
# Barista-2 finished brewing...
# total time taken:9.09 seconds