class demoClass:
    """demo class"""
    name = "lance"
    age = 0

    def __init__(self, name):
        self.name = name
        age = 10

    def demo(self):
        print "demo" + self.name + str(self.age)
