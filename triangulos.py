import psycopg2
from tabulate import tabulate
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
    cursor.execute("INSERT INTO triangulos(l1, l2, l3, triangulo) VALUES (%s, %s, %s, %s);", (x, y, z, w))
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
    cursor.execute("SELECT * from triangulos;")
    print(tabulate(cursor, headers=["ide", "l1", "l2", "l3", "triangulo"], tablefmt="orgtbl", numalign ="center"))


while True:
    try:
        print("Elija una opcion: 1. Mostrar que tipo de triangulo es por sus lados,   2. Historial: \n")
        x=int(input("Opcion a elegir: \n"))
        if x>3 or x<=0:
            print("Numero erroneo, vuelva a ingresar: \n")

        if x==1:
            l1=input("Introduce el primer lado del triangulo: ")
            l2=input("Introduce el segundo lado del triangulo: ")
            l3=input("Introduce el tercer lado del triangulo: ")
            triangulo=""
            
            if l1==l2 and l1==l3 and l2==l3:
                print("Es un triangulo Equilatero \n")
                triangulo="Equilatero"
            
            if (l1==l2 and l1!=l3)or(l1==l3 and l1!=l2)or(l2==l3 and l2!=l1):
                print("Es un triangulo Isoceles \n")
                triangulo="Isoceles"
            
            
            if l1!=l2 and l1!=l3 and l2!=l3:
                print("Es un triangulo Escaleno \n")
                triangulo="Escaleno"
            post(l1, l2, l3, triangulo)
            break
        if x==2:
            ret()
            break
    except Exception as es:
        print("\n Ingreso un caracter y no un numero, vuelva a intentar:\n")
        print(repr(es))
exit(0)