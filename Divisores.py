import psycopg2
from tabulate import tabulate
def  post(x,y):
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
    cursor.execute("INSERT INTO divisores(numero_in, divisores) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()

mat=[]
print("Introduce un número para mostrar sus divisores: ")
x=int(input())
for i in range(1, x+1):
    if x%i==0:
     mat.append(i)
print("Los divisores del numero son: \n ",mat)
post(x,mat)
    