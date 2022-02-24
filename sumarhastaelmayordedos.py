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
    cursor.execute("INSERT INTO ordenarmayamen(pn, sn, res) VALUES (%s, %s, %s);", (x, y, z))
    conexion.commit()
    cursor.close()
    conexion.close()
mat=[]
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero:  "))
if a>b:
    for y in range(a,b-1,-1):
        mat.append(y)
if b>a:
    for y in range(b,a-1,-1):
        mat.append(y)

print("La sucesion es: \n ",mat)
post(a,b,mat)