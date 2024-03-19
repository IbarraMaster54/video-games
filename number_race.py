#imports
from random import randint
import os

#Variables
numJugadoresOk = False
nivelOk = False

numJugadores = None
nivel = None

tamañoTablero = None

posiciones = [0, 0, 0, 0]



#Funciones
def lanzarDados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2;

#Main


print('¡BIENVENIDO!')
#Usuario selecciona el numero de jugadores
while(not numJugadoresOk):
    numJugadores = input('Seleccione el numero de jugadores:')
    if(numJugadores=='2' or numJugadores=='3' or numJugadores=='4'):
        numJugadoresOk = True;
        #Usuario selecciona el nivel de la partida
        while(not nivelOk):
            nivel = input('''Seleccione un nivel para jugar:
                            \n1. Nivel básico (Tablero de 20 posiciones)
                            \n2. Nivel intermedio (Tablero de 30 posiciones)
                            \n3. Nivel avanzado (Tablero de 50 posiciones)
                            \n4. Nivel experto (Tablero de 100 posiciones)''')

            if(nivel=='1' or nivel=='2' or nivel=='3' or nivel=='4'):
                if(nivel=='1'):
                    tamañoTablero = 20
                elif(nivel=='2'):
                    tamañoTablero = 30
                elif(nivel=='3'):
                    tamañoTablero = 50
                elif(nivel=='4'):
                    tamañoTablero = 100

                nivelOk = True;
                os.system('cls')
            else:
                os.system('cls')
                print('Debes seleccionar un nivel valido.')
    else:
        os.system('cls')
        print('Deben haber minimo 2 y maximo 4 jugadores')


while(True):
    for i in range(int(numJugadores)):
        
        play = input('Jugador ' + str(i+1) + ' Presione Enter para lanzar los dados:')
        os.system('cls')
        dado1, dado2 = lanzarDados()
        print('Dado uno: ',dado1,"\nDado 2: ",dado2)
        posiciones[i] += dado1+dado2 
        print('Jugador ',i+1,', Esta en la posicion: ', posiciones[i],' del tablero\n')
        

        if(dado1==dado2):
            print('Ha sacado pares, puede volver a lanzar los dados por segunda vez.')
            play = input('Jugador ' + str(i+1) + ' Presione Enter para lanzar los dados por segunda vez consecutiva:')
            os.system('cls')
            dado1, dado2 = lanzarDados()
            print('Dado uno: ',dado1,"\nDado 2: ",dado2)
            posiciones[i] += dado1+dado2 
            print('Jugador ',i+1,', Esta en la posicion: ', posiciones[i],' del tablero\n')

            if(dado1==dado2):
                print('Ha sacado pares por segunda vez, puede volver a lanzar los dados por tercera vez.')
                play = input('Jugador ' + str(i+1) + ' Presione Enter para lanzar los dados por tercera vez consecutiva:')
                os.system('cls')
                dado1, dado2 = lanzarDados()
                print('Dado uno: ',dado1,"\nDado 2: ",dado2)
                posiciones[i] += dado1+dado2 
                print('Jugador ',i+1,', Esta en la posicion: ', posiciones[i],' del tablero\n')

                if(dado1==dado2):
                    print('Felicidades, ha sacado pares por tercera vez consecutiva, ha ganado el juego')
                    break;
        
        if(posiciones[i]>=tamañoTablero):
            print('\nFelicidades jugador #',i+1,', has ganado.')
            break;
    if(posiciones[i]>=tamañoTablero):
            break;