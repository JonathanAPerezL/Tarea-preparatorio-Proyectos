pkg load database;
clc; 
clear all; 
close all;
retry= true;

while retry
  try
    fprintf("Elija una opcion: 1. Mostrar que tipo de triangulo es por sus lados,   2. Historial: ");
    y=(input ("Opcion a elegir: "));
    if y>2||y==0||y<0
      fprintf("Numero erroneo, vuelva a ingresar: \n");
    endif
    if y==1
      l1=input('Introduce el primer lado del triangulo: ');
      l2=input('Introduce el segundo lado del triangulo: ');
      l3=input('Introduce el tercer lado del triangulo: ');
      triangulo='';
        if l1==l2&&l1==l3&&l2==l3
           fprintf('Es un triangulo Equilatero \n');
           triangulo='Equilatero';
        endif
        
        if (l1==l2 && l1~=l3)||(l1==l3 & l1~=l2)||(l2==l3 & l2~=l1)
            fprintf('Es un triangulo Isoceles \n'); 
            triangulo='Isoceles';
        endif
        
        if l1~=l2&&l1~=l3&&l2~=l3
            fprintf('Es un triangulo Escaleno \n'); 
            triangulo='Escaleno';
        endif

            %Conectar con PGADMIN
            params=cell(1,4);
            params{1,1}=l1;
            params{1,2}=l2;
            params{1,3}=l3;
            params{1,4}=triangulo;


            conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
            'port','5432','user','postgres','password','jblue5queso'));
            N=pq_exec_params(conn, "insert into triangulos(l1,l2,l3,triangulo) values($1,$2,$3,$4);",params); %insertar datos en la tabla

            %Texto
            save('triangulos.txt','l1','l2','l3','triangulo','-ascii');
            retry=false;
        endif
     if y==2
       conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
       'port','5432','user','postgres','password','jblue5queso'));
       N=pq_exec_params(conn, "Select*from triangulos;"); %historial de la tabla
       disp(N)
       retry=false;
     endif
      catch
      fprintf("Solo se permiten valores numericos, vuelava a selecionar %d \n");
      msg = lasterror.message;
      fprintf(msg);
    end_try_catch
  endwhile
