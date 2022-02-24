import psycopg2
import math
from tabulate import tabulate
def  post(x,y,z):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "jblue5queso",
            dbname = "tarea1"
            )
    except:
        print("Sin Conexion Exitosa\n")
            
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO dosendos(n1, n2, res) VALUES (%s, %s, %s);", (x, y, z))
    conexion.commit()
    cursor.close()
    conexion.close()


mat=[]
a = int(input("Ingrese un numero (inicio de la sucesion): "))
b = int(input("Ingrese otro numero (final de la sucesion): "))
for y in range(a,b,2):
    mat.append(y)
print("La sucesion es: \n ",mat)
post(a,b,mat)