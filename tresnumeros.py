
import psycopg2

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
    cursor.execute("INSERT INTO tresnumero(n1, n2, n3) VALUES (%s, %s, %s);", (x, y, z))
    conexion.commit()
    cursor.close()
    conexion.close()

n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el tercer número: "))

if n2<n1 and n3<n1:
     print("El primer numero es el mas grande \n")
     sum=n1+n2+n3
     print("La suma de los numeros es: " ,sum)
  
if n3<n2 and n1<n2:
      print("El segundo numero es el mas grande \n")
      mul=n1*n2*n3
      print("La multiplicacion de los numeros es: " ,mul)
  
  
if n2<n3 and n1<n3:
      print("El tercer numero es el mas grande \n")
      x=str(n1)
      y=str(n2)
      z=str(n3)
      con=x+y+z
      print("El concatenado es: ", con)
  
  
if n1==n2 and n1==n3 and n3==n2:
    print("Todos los numeros son iguales \n")
    print("El primero num. es: ", n1)
    print("El segundo num. es: ", n2)
    print("El tercero num. es: ", n3)

post(n1, n2, n3)

