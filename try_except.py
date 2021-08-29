try:
    x=4
    y=0
    c=x/y
except ZeroDivisionError:
    print('Nefunguje ti to')
finally:
    print('Tohle je pokazdy')