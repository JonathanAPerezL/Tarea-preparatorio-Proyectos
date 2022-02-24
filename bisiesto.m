pkg load database;
clc; 
clear all; 
close all;
retry= true;

while retry
  try
    fprintf("Elija una opcion: 1. Mostrar si es uño bisiesto,   2. Historial: ");
    y=(input ("Opcion a elegir: "));
    if y>2||y==0||y<0
      fprintf("Numero erroneo, vuelva a ingresar: \n");
    endif
    if y==1
      yer=input('Introduce su año de nacimiento: ');
        if (mod(yer,400)==0)||(mod(yer,4)==0)||(mod(yer,100)==0)
           Es='Bisiesto';
           fprintf("El año es Bisiesto \n");
        elseif
           Es='No es bisiesto'; 
           fprintf("El año no es bisiesto \n");
        endif

            %Conectar con PGADMIN
            params=cell(1,2);
            params{1,1}=yer;
            params{1,2}=Es;
           
            conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
            'port','5432','user','postgres','password','jblue5queso'));
            N=pq_exec_params(conn, "insert into bisiesto(yer,Es) values($1,$2);",params); %insertar datos en la tabla

            %Texto
            save('bisiesto.txt','yer','Es','-ascii');
            retry=false;
        endif
     if y==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select*from bisiesto;"); %historial de la tabla
       disp(N)
       retry=false;
     endif
      catch
      fprintf("Solo se permiten valores numericos, vuelva a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
  endwhile
