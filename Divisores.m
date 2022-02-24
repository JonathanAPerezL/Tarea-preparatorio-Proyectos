pkg load database;
clc; 
clear all; 
close all;

fprintf('Bienvenido ');
n=input('Introduce un numero para mostrar sus divisores: ');
while (n~=fix(n))||(n<0)
  fprintf('Ingrese un valor numerico ');
  n=input(',Digite otro valor de n: ');
end
cont=1;
for i=1:n
    x=mod(n,i);
    if x==0
        V(cont)=i;
        cont=cont+1;    
    endif
end    
fprintf('Los divisores de %i son: ',n)
disp(V)

%Conectar con PGADMIN
linearecta=mat2str(V);
params= cell(1,2);
params{1,1}=n;
params{1,2}=linearecta;


conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into divisores(numero_in,divisores) values($1,$2);",params); %insertar datos en la tabla

%Texto
save('Divisores.txt','V','-ascii');