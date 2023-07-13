from vikingsClasses import *
import random

nombres = ['Juan', 'Pedro', 'María', 'Ana', 'Luis', 'Carla', 'Sofía', 'Miguel', 'Antonio', 'Isabel',
           'Manuel', 'José', 'Laura', 'Diego', 'David', 'Javier', 'Rosa', 'Julia', 'Ricardo', 'Fernando',
           'Silvia', 'Gabriel', 'Paola', 'Raúl', 'Rubén', 'Ángela', 'Lorena', 'Pablo', 'Camila', 'Simón',
           'Patricia', 'Sara', 'Santiago', 'Lucía', 'Daniel', 'Víctor', 'Elena', 'Diana', 'Lidia', 'Cristina',
           'Emilia', 'Marcela', 'Eduardo', 'Felipe', 'Jorge', 'Claudia', 'Renata', 'Andrés', 'Marina']

strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
            27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
            75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

ejercito = [1, 2]


# Creación de los dos ejércitos
war = War()

for i in nombres:
    st = random.choice(strength)
    ej = random.choice(ejercito)
    if ej == 1:
        vikingo = Viking(i, 100, st)
        war.addViking(vikingo)
    elif ej == 2:
        saxon = Saxon(100, st)
        war.addSaxon(saxon)
    else:
        pass


# Comenzamos la batalla
progress = True
viking_turn = True
while progress:
    if len(war.saxonArmy) > 0 and len(war.vikingArmy) > 0:
        if viking_turn:
            war.vikingAttack()
            if len(war.saxonArmy) > 0:
                print(war.showStatus())
                viking_turn = False
            else:
                print(war.showStatus())
                progress = False
        else:
            war.saxonAttack()
            if len(war.vikingArmy) > 0:
                print(war.showStatus())
                viking_turn = True
            else:
                print(war.showStatus())
                progress = False
    else:
        print(war.showStatus())
