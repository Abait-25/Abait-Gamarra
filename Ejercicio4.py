#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:


numero=int(input("digite un entero positivo :   "))
SumaN=numero*(numero+1)/2

print(f" La suma de los primeros {numero} numeros es {SumaN}")
