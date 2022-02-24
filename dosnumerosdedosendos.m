pkg load database;
clc; 
clear all; 
close all;
uno = input('Ingrese un numero (inicio de la sucesion): ');
dos = input('Ingrese otro numero (final de la sucesion): ');
sum=1;
for x=uno:2:dos
  V(sum)=x;
  sum=sum+1;
endfor
disp(V)

%Conectar con PGADMIN
linearecta=mat2str(V);
params= cell(1,3);
params{1,1}=uno;
params{1,2}=dos;
params{1,3}=linearecta;


conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into dosendos(n1,n2,res) values($1,$2,$3);",params); %insertar datos en la tabla

%Texto
save('dosnumerosdedosendos.txt','uno','dos','V','-ascii');