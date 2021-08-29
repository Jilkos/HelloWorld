import socket
import argparse

## get switch pro command line args
# todo ... byl zapnuty prepinac d nebo i?
parser = argparse.ArgumentParser(description='Preklad jmen na dresy a opacne')
parser.add_argument('-i', action='store_true', default=False, help='budu hledat jmeno z adresy')
parser.add_argument('-d', action='store_true', default=False, help='budu hledat adresu z jmena')
args=parser.parse_args()
##

# mam i
if args.i:
    try:
        print(socket.gethostbyaddr(input("Zadej adresu: ")))
    except:
        print("Zadej spravnou adresu supaku")

elif args.d:
    # mam d
    try:
        print(socket.gethostbyname(input("Zadej domenu: ")))
    except:
        print("Zadej spravnou domenu supaku")