clc; 
clear all; 
close all;

retry= true;
while retry
  try
    fprintf("Elija una opcion: (1.Promedio y estado del alumno,   2.Historial)");
    i=(input ("\n Opcion a elegir: "));
    if i>3||i<0
      fprintf("\n Numero erroneo, vuelva a ingresar: ");
    endif
    if i==1
      n1=(input('Ingrese la primer nota: '));
      n2=(input('Ingrese la segunda nota: '));
      n3=(input('Ingrese la tercera nota: '));
      prom=((n1+n2+n3)/3);
      if 60<prom||60==prom
          fprintf('Alumno Aprobado \n');
          estado='Aprobado';
          fprintf('El promedio de notas es: %d \n', prom);
      endif
      if 60>prom
          fprintf('Alumno Reprobado \n');
          estado='Reprobado';
          fprintf('El promedio de notas es: %d \n', prom);
      endif
      %Conectar con PGADMIN
      conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
      'port','5432','user','postgres','password','jblue5queso'));
      params=cell(1,5);
      params{1,1}=n1;
      params{1,2}=n2;
      params{1,3}=n3;
      params{1,4}=prom;
      params{1,5}=estado;
      N=pq_exec_params(conn, "insert into notas(n1, n2, n3, promedio, estado) values($1,$2,$3,$4,$5);",params); %insertar datos en la tabla
      %Texto
      save('notas.txt','n1', 'n2', 'n3', 'prom','estado','-ascii');

    endif
    if i==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select * from notas;");%historial de la tabla
       disp(N);
       retry=false;
    endif
 
  catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
 endwhile