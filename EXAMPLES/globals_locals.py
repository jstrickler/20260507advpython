from pprint import pprint  # import prettyprint function

# global variables
count = 42  
animal = 'Wombat'

def spam(fruit):  # function parameters are local
    knight = 'Lancelot'  # local variable
    print("Locals:")
    print(f"{id(locals()) = }")
    
    pprint(locals())  # locals() returns dict of all locals
    print()

spam('mango')

# globals() returns dict of all globals
print("Globals:")
pprint(globals())
print()

g = globals()
g['color'] = "blue"  # create a new variable
#  color = "blue"   
print("color:", color)

loc = locals()
print(f"{g is loc = }")
g1 = globals()
g2 = globals()
print(id(g1), id(g2), id(g), id(loc))