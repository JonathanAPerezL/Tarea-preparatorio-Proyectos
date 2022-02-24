pkg load database;
clc; 
clear all; 
close all;

n1=input('Introduce el primer numero: ');
n2=input('Introduce el segundo numero: ');
n3=input('Introduce el tercer numero: ');
sum=0;
mul=0;
  if n2<n1&&n3<n1
     fprintf('El primer numero es el mas grande \n');
     sum=n1+n2+n3;
     fprintf('La suma de los numeros es: %d\n' ,sum);
  endif
  
  if n3<n2&&n1<n2
      fprintf('El segundo numero es el mas grande \n');
      mul=n1*n2*n3;
      fprintf('La multiplicacion de los numeros es: %d\n' ,mul);
  endif
  
  if n2<n3&&n1<n3
      fprintf('El tercer numero es el mas grande \n');
      x=mat2str(n1);
      y=mat2str(n2);
      z=mat2str(n3);
      f= strcat(x, y, z);
      fprintf('El concatenado es: %s \n', f);
  endif
  
  if n1==n2&&n1==n3&&n3==n2
     fprintf('Todos los numeros son iguales \n');
     fprintf('El primero num. es: %d\n', n1);
     fprintf('El segundo num. es: %d\n', n2);
     fprintf('El tercero num. es: %d\n', n3);
  endif

%Conectar con PGADMIN
params= cell(1,3);
params{1,1}=n1;
params{1,2}=n2;
params{1,3}=n3;

conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into tresnumero(n1,n2,n3) values($1,$2, $3);",params); %insertar datos en la tabla

%Texto
save('tresnumeros.txt','n1','n2', 'n3','-ascii');
