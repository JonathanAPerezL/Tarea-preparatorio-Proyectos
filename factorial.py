import math

import psycopg2
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
    cursor.execute("INSERT INTO factorial(num, nom, es) VALUES (%s, %s, %s);", (x, y, z))
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
    cursor.execute("SELECT * from factorial;")
    print(tabulate(cursor, headers=["ide", "num", "nom", "es"], tablefmt="orgtbl", numalign ="center"))


while True:
    try:
        print("Elija una opcion: 1. Factorial,   2. Historial: \n")
        x=int(input("Opcion a elegir: \n"))
        if x>3 or x<=0:
            print("Numero erroneo, vuelva a ingresar: \n")
        if x==1:
            y=int(input("Ingrese un numero para sacar el factorial: "))
            z=y%7
            if z==0:
                fac=math.factorial(y)
                es="Divisible"
                print("Es divisible de 7")
                print("El factorial del numero es: \n", fac)
                post(y, fac, es)
            if z!=0:
                fac=0
                es="No es Divisible"
                print("No es divisible de 7")
            post(y, fac, es)
        if x==2:
            ret()
            break
    except Exception as e:
        print("\n Ingreso un caracter y no un numero, vuelva a intentar:\n")
        print(repr(e))
exit(0)
