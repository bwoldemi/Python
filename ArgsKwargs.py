# reference   https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

# understanding *argv **kwargs 
def test_argv(*argv):
    for arg in argv:
        print("the variable %s" %arg)
test_argv("one","two","three")
'''
    the variable one
    the variable two
    the variable three
'''

# kwargs
def test_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print("key = %s value = %s" %(key, value))

test_kwargs(name="Bereket", lastname="Woldemicael")
''''
key = lastname value = woldemicael
key = name value = bereket
'''''