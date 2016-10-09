print('user define function')
def whatsup(x='Smith'):
    return 'whatsup'+ x
print (whatsup())
print (whatsup('tnoy'))

def grocery(*items):
    print (items)
    
grocery('milk','bread','egg')


def profile(name,*course):
    print (name)
    print (course)


profile ('zaianb','simulation','project management')


def cart(**items) :
    print (items)

cart(apples=4,mango=8,banana=12)


print ('Tuples as Parameter')

def example1 (a, b, c):
    return (a + b + c)


tuna=(5,7,3)

print (example1(*tuna))


def example2 (**this):
    print (this)
    

book={'mom':54,'dad':44,'sis':25}
example2 (**book)
