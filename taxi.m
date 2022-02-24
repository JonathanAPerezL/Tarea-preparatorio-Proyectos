clc; 
clear all; 
close all;

retry= true;
while retry
  try
    fprintf("Elija una opcion: (1. Saber la condicion del taxi,   2.Historial)");
    i=(input ("\n Opcion a elegir: "));
    if i>3||i<0
      fprintf("\n Numero erroneo, vuelva a ingresar: ");
    endif
    if i==1
      modelo=(input('Ingrese el modelo del taxi: '));
      recorrido=(input('Ingrese el recorrido en Km del taxi: '));
      if modelo<2007&&20<recorrido
         fprintf('Debe renovarse \n');
         estado='Debe renovarse'; 
      elseif 2007<=modelo<=2013&&20000==recorrido
        fprintf('Debe recibir mantenimiento \n');
        estado='Debe recibir mantenimiento';
      elseif modelo>2013&&10000>recorrido
        fprintf('Esta en optimas condiciones \n');
        estado='Esta en optimas condiciones';
      else
        fprintf('Mecánico \n');
        estado='Mecánico';
      endif
      %Conectar con PGADMIN
      conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
      'port','5432','user','postgres','password','jblue5queso'));
      params=cell(1,3);
      params{1,1}=modelo;
      params{1,2}=recorrido;
      params{1,3}=estado;
      N=pq_exec_params(conn, "insert into taxi(modelo, recorrido_km, estado) values($1,$2,$3);",params); %insertar datos en la tabla
      %Texto
      save('taxi.txt','modelo', 'recorrido','estado','-ascii');
    endif
    if i==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select * from taxi;");%historial de la tabla
       disp(N);
       retry=false;
    endif
   catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
 endwhile