import inspect

def barn():
    chicken()

def chicken():
    eggs()

def eggs():
    print("EGGS")
    # get frame (function call stack) info
    current_frame = inspect.currentframe()
    print("Current frame:", inspect.getframeinfo(current_frame))

barn()