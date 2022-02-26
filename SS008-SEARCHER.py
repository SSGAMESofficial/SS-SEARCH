from colorama import Fore, Back, Style


print(f'{Fore.RED}──────────────────────────────────────────────────────────────────────────')
print(f'{Fore.RED}─██████████████─██████████████─██████████████─██████████████─██████████████─')
print(f'{Fore.RED}─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─')
print(f'{Fore.RED}─██░░██████████─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████░░██─')
print(f'{Fore.RED}─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─')
print(f'{Fore.RED}─██░░██████████─██░░██████████─██░░██──██░░██─██░░██──██░░██─██░░██████░░██─')
print(f'{Fore.RED}─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─')
print(f'{Fore.RED}─██████████░░██─██████████░░██─██░░██──██░░██─██░░██──██░░██─██░░██████░░██─')
print(f'{Fore.RED}─────────██░░██─────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─')
print(f'{Fore.RED}─██████████░░██─██████████░░██─██░░██████░░██─██░░██████░░██─██░░██████░░██─')
print(f'{Fore.RED}─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─')
print(f'{Fore.RED}─██████████████─██████████████─██████████████─██████████████─██████████████─')
print(f'{Fore.RED}────────────────────────────────────────────────────────────────────────────')

print(f'{Fore.BLUE}   1. Mirar Paginas           3.Creditos                                               ')
print(f'{Fore.BLUE}   2. Busqueda                                                                 ')

pedir = input('[>] ')


def buscar():
    Reconmendaciones = """
    Si va a buscar a alguien inserte el nombre de usuario y no el nombre "Real", para que le de una busqueda más exacta
    
    """
    print(f'{Fore.LIGHTMAGENTA_EX} {Reconmendaciones} {Fore.RESET}')
    nombre = input("Por favor ingrese el nombre de USUARIO que quiera buscar: ")
    nombre = str(nombre)
    lista = [
    'https://facebook.com/',
    'https://twitter.com/',
    'https://instagram.com/',
    'https://Linkedln.com/',
    'https://pinterest.com/',
    'https://tiktok.com/@',
    'https://reddit.com/user/',
    'https://snapchat/',
    'https://youtube.com,/',
    'https://twitch.tv/',
    'https://github.com/',
    'https://wattpad.com/user/',
    'https://xbox.com/es-Es/user/',
    'https://pornhub.com/']
    def busqueda():
        print(f'#facebook{Fore.LIGHTRED_EX} {lista[0]}{nombre}{Fore.RESET}')
        print(f'#twitter{Fore.LIGHTRED_EX} {lista[1]}{nombre}{Fore.RESET}')
        print(f'#instagram{Fore.LIGHTRED_EX} {lista[2]}{nombre} {Fore.RESET}')
        print(f'#linkedln {Fore.LIGHTRED_EX} {lista[3]}{nombre}{Fore.RESET}')
        print(f'#pinterest{Fore.LIGHTRED_EX} {lista[4]}{nombre} {Fore.RESET}')
        print(f'#tik tok {Fore.LIGHTRED_EX} {lista[5]}{nombre}{Fore.RESET}')
        print(f'#reddit{Fore.LIGHTRED_EX} {lista[6]}{nombre}{Fore.RESET}')
        print(f'#snapchat{Fore.LIGHTRED_EX} {lista[7]}{nombre} {Fore.RESET}')
        print(f'#youtube{Fore.LIGHTRED_EX} {lista[8]}{nombre} {Fore.RESET}')
        print(f'#twitch{Fore.LIGHTRED_EX} {lista[9]}{nombre} {Fore.RESET}')
        print(f'#github{Fore.LIGHTRED_EX} {lista[10]}{nombre}{Fore.RESET}')
        print(f'#Wattpad{Fore.LIGHTRED_EX} {lista[11]}{nombre} {Fore.RESET}')
        print(f'#XBOX {Fore.LIGHTRED_EX} {lista[12]}{nombre}{Fore.RESET}')
    if pedir == '2':
        busqueda()

    
if pedir == "2":
    buscar()


if pedir == '1':
        paginas = """
1. Facebook
2. tiwtter
3. Instagram
4. Linkdln
5. Pinterest
6. TikTok
7. Reddit
8. SnapChat
9. youtube
10. TwitchTV
11. GitHub
12. Wattpad
13. Xbox
        """
        print(f'{Fore.LIGHTMAGENTA_EX}{paginas}{Fore.RESET}')


if pedir ==  '3':
    GAMA = """
  ooooooo8      o      oooo     oooo      o             ooooooo     ooooooo     ooooooo   
o888    88     888      8888o   888      888          o888  o888o o888  o888o o888   888o 
888    oooo   8  88     88 888o8 88     8  88         888  8  888 888  8  888  888888888  
888o    88   8oooo88    88  888  88    8oooo88        888o8  o888 888o8  o888 888o   o888 
 888ooo888 o88o  o888o o88o  8  o88o o88o  o888o        88ooo88     88ooo88     88ooo88  

 Discord:̶͇͇ ̶͇͇G̶͇͇a̶͇͇m̶͇͇a̶͇͇ ̶͇͇#6245
    """

    SS = """
 SSSSS   SSSSS    GGGG    AAA   MM    MM EEEEEEE  SSSSS  
SS      SS       GG  GG  AAAAA  MMM  MMM EE      SS      
 SSSSS   SSSSS  GG      AA   AA MM MM MM EEEEE    SSSSS  
     SS      SS GG   GG AAAAAAA MM    MM EE           SS 
 SSSSS   SSSSS   GGGGGG AA   AA MM    MM EEEEEEE  SSSSS  
    Discord: 丂丂Ꮆ卂爪乇丂#4909                                                       
"""
    print(f'{Fore.LIGHTMAGENTA_EX} {GAMA} {Fore.RESET}')
    print(f'{Fore.LIGHTGREEN_EX}___________________________________________{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX} {SS} {Fore.RESET}')