import random
# Se importa la librería que trabaja números aleatorios
salir = True #se declara e inicia variable para romper ciclo infinito
while salir:
    #se usa funcion ranint que genera numeros enteros aleatorios
    # entre el rango señalado (inclusivo)
    x, y = random.randint(1,6),random.randint(1,6) 
    print ('El primer dado ha sido:',x)
    print ('El segundo dado ha sido:',y)
    print ('Su resultado es', x + y)
    #se pregunta si se desea tirar otra vez, señalando en nueva línea las opciones correctas
    pregunta = input("Desea tirar otra vez? \n (S,s,SI,Si,si para reintentar)")
    if pregunta != "s" and pregunta != "S" and pregunta != "SI" and pregunta != "Si" and pregunta != "si":
        salir = False #cualquier caracter no esperado rompera el ciclo