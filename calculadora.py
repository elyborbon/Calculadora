numero_1 = int (input ("Escribe un numero: "))
numero_2 = int (input ("Escribe un numero: "))

print ("""Indique la operacion a realizar:"
1) Suma 
2) Resta
3) División
4) Multiplicación
5) Cambiar los numeros introducidos
6) Salir de la calculadora
""")

seleccion =int(input ("Selecciona la operacion que quiera realizar: "))

if seleccion == 1:
    print ("La suma es: ", numero_1 + numero_2)
elif seleccion == 2:
    print ("La resta es: ", numero_1 - numero_2)
elif seleccion == 3:
    print ("La division es: ",float(numero_1/numero_2))
elif seleccion == 4:
    print ("La multiplicacion es: ", numero_1 * numero_2)
elif seleccion == 5:
    print ("Agregue nuevos numeros: ")
    numero_1 = int (input ("Escribe un numero: "))
    numero_2 = int (input ("Escribe un numero: "))
else: 
    print ("Salio de la calculadora")