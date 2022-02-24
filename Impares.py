import psycopg2
import math
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
    cursor.execute("INSERT INTO impares(res, cantidad) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()

def ret():
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
    cursor.execute("SELECT * from impares;")
    print(tabulate(cursor, headers=["ide", "res", "cantidad"], tablefmt="orgtbl", numalign ="center"))

print("Los numeros del 1 al 100 que son impares: \n")
mat=[]
while True:
    try:
        print("Introduce el numero de la operacion a realizar (1.Numeros impares (1-100), 2.Historial, 3.Salir): ")
        x=int(input("Elija:\n"))
        if x>3 or x<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif x==1:
            for y in range(1,100,2):
                mat.append(y)
            print("Los numero impares del 1 al 100 son: \n ",mat)
            post(mat,len(mat))
        elif x==2:
            ret()
        elif x==3:
            break

    except Exception as es:
        print("\n Ingreso un caracter y no un numero, vuelva a intentar:\n")
        print(repr(es))

exit(0)