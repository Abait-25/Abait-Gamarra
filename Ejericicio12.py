"""
Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :

"""

nombre_archivo=input("Digite nombre del archivo :  ")
nombre,extension= nombre_archivo.split(".")
if extension=="gif":
 print("MIME Type:    image/gif")
elif extension=="jpg":
 print("MIME Type: image/jpeg")
elif extension=="jpeg":
 print("MIME Type: image/jpeg")
elif extension=="png":
 print("MIME Type: image/png")
elif extension=="pdf":
 print("MIME Type: application/pdf")
elif extension=="txt":
 print("MIME Type: text/plain")
elif extension=="zip":
 print("MIME Type: application/zip")
else:
 print("MIME Type: application/octet-stream")
