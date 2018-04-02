def strong_decorator(func):
  def func_wrapper(name):
    return "<strong>%s<strong>"%func(name)
  return func_wrapper

def p_decorate(func):
  def func_wrapper(name):
    return "<p>{0}</p>".format(func(name))
  return func_wrapper

def div_decorator(func):
  def func_wrapper(name):
    return "<div>%s<div>"%func(name)
  return func_wrapper

@div_decorator
@p_decorate
@strong_decorator
def get_text(name):
  return "hell %s" %name
  
if __name__=="__main__": 
  print (get_text("bereket"))
