
class Doit:
    def __call__(self):
        print("Doing the thing magically!")

    def  doit(self):
        print("Doing the thing!")

d = Doit()
d.doit()
d()
