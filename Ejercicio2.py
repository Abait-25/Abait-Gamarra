#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.
costo_alimentos=int(input("Digite el monto de su comida "))
Porcentaje_prop=float(input("Que porcentage de su monto le gustaria que sea propina "))
if Porcentaje_prop>=0.15 :
    Propina=costo_alimentos*Porcentaje_prop
    print(f"El monto de la propina es : {Propina} $")
else:
    print("Debe de aportar mas en la propina")