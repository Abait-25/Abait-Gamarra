#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.


payasos=int(input("Numero de payasos en el pedido :  "))
muñecas=int(input("Numero de muñecas en el pedido :  "))

Peso_payasos= payasos*112/1000
Peso_muñecas= muñecas*75/1000
print("el peso total de payasos es de {} Kg y el de muñecas de {} Kg .".format(Peso_payasos,Peso_muñecas))