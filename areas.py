import psycopg2
from tabulate import tabulate
import numpy as np
def  post(x,y,z,w):
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
    cursor.execute("INSERT INTO areas(figura, largo, altura, area) VALUES (%s, %s, %s, %s);", (x, y, z, w))
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
    cursor.execute("SELECT * from areas;")
    print(tabulate(cursor, headers=["ide", "figura", "largo", "altura", "area"], tablefmt="orgtbl", numalign ="center"))

while True:
    try:
        print("Elija una opcion: (1.Areas de figuras,   2.Historial,   3.Salir)")
        x=int(input("Elija la opcion:\n"))
        if x>3 or x<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif x==1:
            while True:
                try:
                    print("Que figura necesita calcular el area\n")
                    print("Elija una opcion: (1.Circulo,  2.Triangulo,  3.Cuadrado,  4.Rectangulo")
                    radio=int(input("Elija:\n"))
                    altura=0
                    if radio>4 or x<=0:
                        print("Valor ingresado fuera del rango del menu.\n")
                    if radio==1:
                        ra=int(input("Ingrese el radio del Circulo:\n"))
                        fig="Circulo"
                        a=np.pi*pow(ra,2)
                    if radio==2:
                        ra=int(input("Ingrese  la base del Triangulo:\n"))
                        altura= int(input("Ingrese la altura del triangulo:\n"))
                        fig="Triangulo"
                        a=ra*altura*1/2
                    if radio==3:
                        ra=int(input("Ingrese  el lado del cuadrado:\n"))
                        altura = ra
                        a= pow(ra,2)
                        fig="Cuadrado"
                    if radio==4:
                        ra = int(input("Ingrese la base del rectangulo\n"))
                        altura = int(input("Ingrese la altura del rectangulo\n"))
                        a=ra*altura
                        fig="Rectangulo"
                    print("El Area del "+ fig+" es:"+str(a))
                    post(fig, ra, altura, a)
                    break 
                except Exception as e:
                    print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
                    print(repr(e))
        elif x==2:
            ret()
        elif x==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)