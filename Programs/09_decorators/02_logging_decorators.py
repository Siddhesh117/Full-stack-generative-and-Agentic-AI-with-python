from functools import wraps

def log_activity(fun):
    @wraps(fun)
    def wrapper(*args, **Kwargs):
        print(f"Calling: {fun.__name__}")
        result = fun(*args, **Kwargs)
        print(f"Finished: {fun.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")
# Calling: brew_chai
# Brewing Masala chai and milk status no
# Finished: brew_chai