import sys
#en la siguiente línea se va a evaluar si la cantidad de argumentos ingresados son 2, sino largará un error
if len(sys.argv) == 2:
    import datetime
    import os

    marcadetiempo = datetime.datetime.now()
    marcadetiempo = int(datetime.datetime.timestamp(marcadetiempo))

    lluvia = sys.argv [1]
    temperatura = input ("Ingrese la temperatura en grados centígrados: ")
    humedad = input ("Ingrese el porcentaje de humedad: ")
    lineadeescr = str(marcadetiempo) + "," + temperatura + "," + humedad + "," + lluvia

    vararch = open ("clase10_ej2.csv", "a")
    vararch.write (lineadeescr + "\n")
    vararch.close()
else:
    print ("La cantidad de argumentos ingresados son menores a 2")
    print ("La manera correcta es por ejemplo, <.\clase10_ej2.py> <True o False>")