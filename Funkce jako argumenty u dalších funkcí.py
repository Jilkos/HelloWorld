def shout(word):
    """Print a word wtih an exclamation mark
    following it"""
    print(word+'!')
shout('spam')
"""Operace lec gou bejbi"""
a=4
b=2
def multiply(x, y):
    return x*y
operation=multiply
print(operation(a,b))
"""Tohle je fakt sranda XD"""
def add(x,y):
    return x+y

def do_twice(func,x,y):
    return func(func(x,y), func (x,y))
c=5
d=10
print(do_twice(add,c,d))