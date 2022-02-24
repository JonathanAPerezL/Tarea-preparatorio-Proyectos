
import psycopg2
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
    cursor.execute("INSERT INTO sumarhastan(n, suma) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()


print("Ingrese el valor final de la sumatoria: ")
a = int(input())
b=0
for i in range(1, a+1):
    b=b+i
print("La suma es: ", b)
post(a, b)