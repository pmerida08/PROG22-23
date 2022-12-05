num1 = int(input("Imprime el primer número que quieres hacerle la operación: "))
num2 = int(input("Imprime el segundo número que quieres hacerle la operación: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

operacion = str(input("Dime que operación quieres hacer: "))

if operacion == "suma":
    print("La suma de los numeros ", num1, " y ", num2, " es: ", suma)
elif operacion == "resta":
    print("La resta de los numeros ", num1, " y ", num2, " es: ", resta)
elif operacion == "mult":
    print("La multiplicación de los numeros ", num1, " y ", num2, " es: ", mult)
elif operacion == "div":
    print("La division de los numeros ", num1, " y ", num2, " es: ", div)
else:
    print("La operacion no existe")
