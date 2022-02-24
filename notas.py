import psycopg2
from tabulate import tabulate

def  post(x,y,z, w, v):
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
    cursor.execute("INSERT INTO notas(n1, n2, n3, promedio, estado) VALUES (%s, %s, %s, %s, %s);", (x, y, z, w, v))
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
    cursor.execute("SELECT * from notas;")
    print(tabulate(cursor, headers=["ide", "n1", "n2", "n3", "promedio", "estado"], tablefmt="orgtbl", numalign ="center"))

while True:
    try:
        print("Elija una opcion: (1. Promedio y estado del alumno,   2.Historial,   3.Salir)")
        x=int(input("Elija la opcion:\n"))
        if x>3 or x<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif x==1:
            estado=""
            n1=int(input("Ingrese la primer nota: "))
            n2=int(input("Ingrese la segunda nota: "))
            n3=int(input("Ingrese la tercera nota: "))
            prom=((n1+n2+n3)/3)
            if 60<prom or 60==prom:
                print("Alumno Aprobado")
                estado="Aprobado"
                print("El promedio de notas es: " + str(prom))
            
            if 60>prom:
                print("Alumno Reprobado")
                estado="Reprobado"
                print("El promedio de notas es: " + str(prom))
            post(n1, n2, n3, prom, estado)
        elif x==2:
            ret()
        elif x==3:
            break
    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)