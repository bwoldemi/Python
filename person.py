
"""
Examples of simple class 
"""
class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def greet(self):
        return " Welcome {0} {1}".format(self.firstname, self.lastname)
        #return "Welcome" + self.firstname

p = Person("Abebe", "Kebede")
greeting = p.greet()
print(greeting)
