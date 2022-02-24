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
    cursor.execute("INSERT INTO taxi(modelo, recorrido_Km, estado) VALUES (%s, %s, %s);", (x, y, z))
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
    cursor.execute("SELECT * from taxi;")
    print(tabulate(cursor, headers=["ide", "modelo", "recorrido_km", "estado"], tablefmt="orgtbl", numalign ="center"))

while True:
    try:
        print("Elija una opcion: (1. Saber la condicion del taxi,   2.Historial,   3.Salir)")
        x=int(input("Elija la opcion:\n"))
        if x>3 or x<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif x==1:
            estado=""
            modelo=int(input("Ingrese el modelo del taxi: "))
            recorrido=int(input("Ingrese el recorrido en Km del taxi: "))
            if modelo<2007 and 20<recorrido:
                print("Debe renovarse")
                estado="Debe renovarse"
            
            elif 2007<=modelo<=2013 and 20000==recorrido:
                print("Debe recibir mantenimiento")
                estado="Debe recibir mantenimiento"

            elif modelo>2013 and 10000>recorrido:
                print("Esta en optimas condiciones")
                estado="Esta en optimas condiciones"
            else:
                print("Mecánico")
                estado="Mecánico"
            post(modelo, recorrido, estado)
        elif x==2:
            ret()
        elif x==3:
            break
    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)