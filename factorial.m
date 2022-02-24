pkg load database;

clc; 
clear all; 
close all;

retry= true;
res=1;
nom=0;
es="";
while retry
  try
    fprintf("Elija una opcion: 1. Factorial,   2. Historial: ");
    i=(input ("\n Opcion a elegir: "));
    if i>2||i==0||i<0
      fprintf("\n Numero erroneo, vuelva a ingresar: ");
    endif
    if i==1
      y=input("Ingrese un numero para sacar el factorial: ")
      z=mod(y,7);
      if z==0
        es="Divisible"
        for x=y:-1:1
          res=res*x;
        endfor
        fprintf("El factorial del numero es: %d \n", res);
        
        %Conectar con PGADMIN
        conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
        'port','5432','user','postgres','password','jblue5queso'));
        params=cell(1,3);
        params{1,1}=y;
        nom=res;
        params{1,2}=nom;
        params{1,3}=es;
        N=pq_exec_params(conn, "insert into factorial(num, nom, es) values($1,$2,$3);",params); %insertar datos en la tabla
        %Texto
        save('factorial.txt','y','nom','es','-ascii');
        retry=false;
      endif
      if z~=0
        fprintf("El numero ingresado no es divisible entre 7\n");
        es="No divisible";
        conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
        'port','5432','user','postgres','password','jblue5queso'));
        params=cell(1,3);
        params{1,1}=y;
        params{1,2}=nom;
        params{1,3}=es;
        N=pq_exec_params(conn, "insert into factorial(num, nom, es) values($1,$2,$3);",params);
        save('factorial.txt','y','nom','es','-ascii');
        retry=false;
      endif
    endif
    if i==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select * from factorial;");%historial de la tabla
       disp(N);
       retry=false;
    endif
   catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
 endwhile
 