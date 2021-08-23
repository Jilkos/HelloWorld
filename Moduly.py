"""Generátor náhodných čísel od 123 do 456."""
import random

for x in range(20):
    value=random.randint(123,456)
    print(value)

"""Když chci něco jen z nějakého modulu můžu použít form ... 
Př. import pi konstanty z matematického modulu"""
from math import pi
print(pi)
"""Hvězdička z modulu importuje všechno, ale nedoporučuju"""
"""Můžeme si to přejmenovat"""
from math import sqrt as square_root
print(square_root(100))

