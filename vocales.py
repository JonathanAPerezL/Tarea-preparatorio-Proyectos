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
    cursor.execute("INSERT INTO letras2(palabra, n) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()


palabra = input("Ingrese su palabra: ")
palabra = palabra.lower()
voca= ["a","e","i","o","u"]
veces=0
for x in range(len(palabra)):
    y=palabra[x]
    if y == voca[0]:
        veces=veces+1
    elif y == voca[1]:
        veces=veces+1
    elif y == voca[2]:
        veces=veces+1
    elif y == voca[3]:
        veces=veces+1
    elif y == voca[4]:
        veces=veces+1

print("Hay %d vocales en la palabra %s"%(veces,palabra))
post(palabra,veces)
exit(0)
