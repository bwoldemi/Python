def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self, disc="your name is"):
        return  disc + " "+ self.name+" "+self.family
my_person = Person()

print my_person.get_fullname()

'''
<p>your name is John Doe</p>
'''
