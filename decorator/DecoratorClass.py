
def p_decorator(func):
    def func_wraper(self):
        return "<p>%s<p>"%func(self)
    return func_wraper

class Person(object):
    def __init__(self):
        self.name="bereket"
        self.fname="woldemicael"

    @p_decorator
    def get_fullname(self):
        return self.name+" " + self.fname
        
if __name__=="__main__":
    name = Person()
    print(name.get_fullname())
        
