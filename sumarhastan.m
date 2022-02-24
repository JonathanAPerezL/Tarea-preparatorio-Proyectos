clc; 
clear all; 
close all;
num = input('Ingrese el numero final de la sumatoria: ');
sum=0;
for x=0:1:num
  sum=sum+x;
end

fprintf('El resultado de la sumatoria es: %d\n', sum)

%Conectar con PGADMIN
params= cell(1,2);
params{1,1}=num;
params{1,2}=sum;

conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into sumarhastan(n,suma) values($1,$2);",params); %insertar datos en la tabla

%Texto
save('sumarhastan.txt','num','sum','-ascii');
