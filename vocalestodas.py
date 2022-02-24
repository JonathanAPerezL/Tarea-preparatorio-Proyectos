import psycopg2
def  post(x,y,z,w,u,v):
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
    cursor.execute("INSERT INTO letras(palabra, na, ne, ni, n0, nu) VALUES (%s, %s, %s, %s, %s, %s);", (x, y, z, w, u, v))
    conexion.commit()
    cursor.close()
    conexion.close()

strt = str(input("Ingrese su palabra:"))

vocales=['a','e','i','o','u']
cantidad=[0,0,0,0,0]

for x in range(0, len(strt)):
    if strt[x]== vocales[0]:
        cantidad[0]=cantidad[0]+1
    if strt[x]== vocales[1]:
        cantidad[1]=cantidad[1]+1
    if strt[x]== vocales[2]:
        cantidad[2]=cantidad[2]+1
    if strt[x]== vocales[3]:
        cantidad[3]=cantidad[3]+1
    if strt[x]== vocales[4]:
        cantidad[4]=cantidad[4]+1
print("Las veces de la vocal a en la palabra es de: \n", cantidad[0])
print("Las veces de la vocal e en la palabra es de: \n", cantidad[1])
print("Las veces de la vocal e en la palabra es de: \n", cantidad[2])
print("Las veces de la vocal o en la palabra es de: \n", cantidad[3])
print("Las veces de la vocal u en la palabra es de: \n", cantidad[4])
post(strt, cantidad[0], cantidad[1], cantidad[2], cantidad[3], cantidad[4])
exit(0)