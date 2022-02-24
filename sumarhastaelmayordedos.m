pkg load database;
clc; 
clear all; 
close all;
pri = input('Ingrese el primer numero: ');
seg = input('Ingrese el segundo numero: ');
sum=1;
params= cell(1,3);
if pri>seg
    params{1,1}=pri;
    params{1,2}=seg;
  for x=pri:-1:seg
    V(sum)=x;
    sum=sum+1;
  endfor
endif

if seg>pri
    params{1,1}=seg;
    params{1,2}=pri;
  for x=seg:-1:pri
    V(sum)=x;
    sum=sum+1;
    
  endfor
endif

disp(V)

%Conectar con PGADMIN
linearecta=mat2str(V);
params{1,3}=linearecta;

conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into ordenarmayamen(pn,sn,res) values($1,$2,$3);",params); %insertar datos en la tabla

%Texto
save('sumarhastaelmayordedos.txt','V','-ascii');