clc; 
clear all; 
close all;

retry= true;
ra=0;
a=0;
altura=0;
while retry
  try
    fprintf("Elija una opcion: (1.Areas de figuras,   2.Historial)");
    i=(input ("\n Opcion a elegir: "));
    if i>3||i<0
      fprintf("\n Numero erroneo, vuelva a ingresar: ");
    endif
    if i==1
      fprintf("Elija una opcion: (1.Circulo,  2.Triangulo,  3.Cuadrado,  4.Rectangulo)");
      x=(input ("\n Opcion a elegir: "));
      if x==1
         ra=(input("Ingrese el radio del Circulo:\n"));
         fig="Circulo";
         a=pi*ra^2;
      endif
      if x==2
          ra=(input("Ingrese  la base del Triangulo:\n"));
          altura= (input("Ingrese la altura del triangulo:\n"));
          fig="Triangulo";
          a=ra*altura*1/2;
      endif
      if x==3
          ra=(input("Ingrese  el lado del cuadrado:\n"));
          altura = ra;
          a=ra^2;
          fig="Cuadrado";
      endif
      if x==4
          ra = (input("Ingrese la base del rectangulo\n"));
          altura =(input("Ingrese la altura del rectangulo\n"));
          a=ra*altura;
          fig="Rectangulo";
      endif
      fprintf("El Area del %s es: %d \n", fig, a);
      %Conectar con PGADMIN
      conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
      'port','5432','user','postgres','password','jblue5queso'));
      params=cell(1,4);
      params{1,1}=fig;
      params{1,2}=ra;
      params{1,3}=altura;
      params{1,4}=a;
      N=pq_exec_params(conn, "insert into areas(figura, largo, altura, area) values($1,$2,$3,$4);",params); %insertar datos en la tabla
      %Texto
      save('areas.txt','fig', 'ra', 'altura', 'a','-ascii');

    endif
    if i==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select * from areas;");%historial de la tabla
       disp(N);
       retry=false;
    endif
   catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
 endwhile
 
 
 