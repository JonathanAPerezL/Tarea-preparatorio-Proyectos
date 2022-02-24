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
    cursor.execute("INSERT INTO bisiesto(yer, es) VALUES (%s, %s);", (x, y))
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
    cursor.execute("SELECT * from bisiesto;")
    print(tabulate(cursor, headers=["ide", "yer", "es"], tablefmt="orgtbl", numalign ="center"))


while True:
    try:
        print("Elija una opcion: 1. Mostrar si su año de nacimiento es bisiesto,   2. Historial: \n")
        x=int(input("Opcion a elegir: \n"))
        if x>3 or x<=0:
            print("Numero erroneo, vuelva a ingresar: \n")

        if x==1:
            yea = int(input("Introduce un año: "))

            if yea % 4 == 0:
                if yea % 100 == 0:
                    if yea % 400 == 0:
                        print("El año es bisiesto")
                        Es="Bisiesto"
                    else:
                        print("El año no es bisiesto")
                        Es="No es bisiesto"
                else:
                    print("El año es bisiesto")
                    Es="Bisiesto"
            else:
                print("El año no es bisiesto")
                Es="No es bisiesto"
            post(yea, Es)
            break
        if x==2:
            ret()
            break
    except Exception as es:
        print("\n Ingreso un caracter y no un numero, vuelva a intentar:\n")
        print(repr(es))
exit(0)