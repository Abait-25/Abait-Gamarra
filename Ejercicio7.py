"""
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

"""
n1=int(input("primer numero:  "))
n2=int(input("segundo numero:  "))
opcion=int(input("Digite que opcion desea realizar: \n 1.suma \n 2.resta \n 3.multiplicacion:  \n  "))
if opcion==1:
    print(f"Suma: {n1+n2}")
elif opcion==2:
    print(f"resta: {n1-n2}")
elif opcion==3:
    print(f"producto: {n1*n2}")
else:
    print("no es correcta esa opcion")