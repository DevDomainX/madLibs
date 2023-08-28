#!/user/bin/env python3
from time import sleep
from colorama import init, Fore, Style
init()
created = """
    created by : Hans Saldias
    
    Script : mad libs 1
    
    Site : 1LugarParaProgramar """
logo = """

'##::::'##::::'###::::'########::::::::::::'##::::: ::'####:'########:::'######::
 ###::'###:::'## ##::: ##.... ##:::::::::: ##:::::::. ##:: ##.... ##:'##... ##:
 ####'####::'##:. ##:: ##:::: ##:::::::::: ##:::::::: ##:: ##:::: ##: ##::: ..::
 ## ### ##:'##:::. ##: ##:::: ##:'#######: ##::::::::: ##:: ########::. ######::
 ##. #: ##: #########: ##:::: ##:.......: ##::::::::: ##:: ##. ... ##::..... ##:
 ##:.:: ##: ##.... ##: ##:::: ##:::::::::: ##::::::::: ##:: ##:::: ##:'##::: ##:
 ##:::: ##: ##:::: ##: ########::::::::::: ########:'### #: ########::. ######::
..:::::..::..::::::..::..........:::::::::::::....... ::....::.......:::::......:::
'########::'#######::'########::::'########::'#### ###::'########:              
..... ##::'##.... ##: ##.....:::::..... ##::'##.... ##: ##.....::              
:::: ##::: ##:::: ##: ##::::::::::::::: ##::: ##:::: ##: ## :::::::              
::: ##:::: ##:::: ##: ######::::::::: ##:::: ##:::: ##: ## ####:::              
:: ##::::: ##:::: ##: ##...::::::::: ##::::: ##:::: ##: ## ...::::              
: ##:::::: ##:::: ##: ##::::::::::: ##:::::: ##:::: ##: ## :::::::              
 ########:. #######:: ########:::: ########:. #######:: ########:              
........:::.......:::...........:::::..........:::..... ..:::.......:::
    """
print(Fore.CYAN+Style.BRIGHT+logo)
for i in created:
    print(i, end="", flush=True)
    sleep(0.1)


e1 = input("\n¿que ladra y es hembra? : ")
e2 = input("¿ que es ser cuatripodo ?: ")
e3 = input("¿ sinonimo de oscuro ?: ")
e4 = input("¿ por donde eschuchamos ?: ")
e5 = input("¿ mas facil que quitarle un _ a un niño? : ")
e6 = input("¿ sinonimo de propietaria?: ")
e7 = input("¿ marca de comida de perro?: ")
e8 = input("¿ nombre de tu mascota?: ")
e9 = input("¿ sinonimo de jefa?: ")
e10 = input("¿ donde mas te gusta visitar?: ")
e11 = input("¿sinonimo de perseguir?: ")
e12 = input("¿sinonimo de encontrar?: ")
e13 = input("¿ sinonimo de pillar ?: ")
e14 = input("¿ sinonimo de regresar?: ")


history = f"Habia una vez, una {e1} que caminaba en {e2} patas, tenia el {e3} negro las {e4} largas. Era muy {e5}  y juguetona con {e6}, comia {e7} veces al dia, ella se llamaba {e8} y amaba a {e9} la seguia para {e10} . Al ir a comprar su dueña ella la {e11} escondida para que no la {e12} pero siempre la {e13} y la echaban de {e14}"

for i in history:
    print(i, end = "", flush = True)
    sleep(0.1)
    
print("1LugarParaProgramar\t\tAuthor: Hans saldias")





