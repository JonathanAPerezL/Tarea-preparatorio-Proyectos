pkg load database;

clc; 
clear all; 
close all;

retry= true;

while retry
  try
    fprintf("Elija una opcion: 1. Mostrar los numeros impares,   2. Historial: ");
    y=(input ("Opcion a elegir: "));
    if y>2||y==0||y<0
      fprintf("Numero erroneo, vuelva a ingresar: \n");
    endif
    
    if y==1
      imp=1;
      for x=1:2:100
        V(imp)=x;
        imp=imp+1;
      endfor
      disp(V)
     %Conectar con PGADMIN
      res=imp-1;
      linearecta=mat2str(V);
      params=cell(1,2);
      params{1,2}=res;
      params{1,1}=linearecta;


      conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
      'port','5432','user','postgres','password','jblue5queso'));
      N=pq_exec_params(conn, "insert into impares(res, cantidad) values($1,$2);",params); %insertar datos en la tabla

      %Texto
      save('impares.txt','V','-ascii');
      retry=false;
    endif
     if y==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select*from impares;"); %historial de la tabla
       disp(N)
       retry=false;
     endif
      catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
  endwhile

  
  