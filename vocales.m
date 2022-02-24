clc; 
clear all; 
close all;
strt = input('Ingrese el texto:   ','s');
Vocales=['a','e','i','o','u'];
mat=[];
for i=1:5
    mat=[mat strfind(strt,Vocales(i))];
end
%Conectar con PGADMIN
cv=length(mat);
fprintf("La cantidad de vocales en el texto es: %d \n",cv);
s=mat2str(cv);
params{1,1}=strt;
params{1,2}=cv;
%Texto
save('vocales.txt','cv','-ascii');
conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into letras2(palabra, n) values($1,$2);",params); %insertar datos en la tabla
