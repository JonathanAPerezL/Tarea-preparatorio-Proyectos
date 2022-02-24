clc; 
clear all; 
close all;
strt = input('Ingrese su palabra:  ','s');
vocales=['a','e','i','o','u'];
cantidad=[0,0,0,0,0];
  for x=1:1:length(strt);
    if strt(x) == vocales(1)
      cantidad(1)=cantidad(1)+1;
    endif
    if strt(x) == vocales(2)
      cantidad(2)=cantidad(2)+1;
    endif
    if strt(x) == vocales(3)
      cantidad(3)=cantidad(3)+1;
    endif
    if strt(x) == vocales(4)
      cant(4)=cantidad(4)+1;
    endif
    if strt(x) == vocales(5)
      cant(5)=cantidad(5)+1;

    endif
    endfor
%Conectar con PGADMIN
disp(cantidad);
fprintf('\n Las veces de la vocal a en la palabra es de: %d', cantidad(1));
fprintf('\n Las veces de la vocal e en la palabra es de: %d', cantidad(2));
fprintf('\n Las veces de la vocal i en la palabra es de: %d', cantidad(3));
fprintf('\n Las veces de la vocal o en la palabra es de: %d', cantidad(4));
fprintf('\n Las veces de la vocal u en la palabra es de: %d\n', cantidad(5));

params= cell(1,6);
params{1,1}=strt;
params{1,2}=cantidad(1);
params{1,3}=cantidad(2);
params{1,4}=cantidad(3);
params{1,5}=cantidad(4);
params{1,6}=cantidad(5);

%Texto
save('vocalestodas.txt','strt','cantidad','-ascii');
conn = pq_connect(setdbopts('dbname','tarea1','host','localhost',
'port','5432','user','postgres','password','jblue5queso'));
N=pq_exec_params(conn, "insert into letras(palabra,na,ne,ni,n0,nu) values($1,$2,$3,$4,$5,$6);",params); %insertar datos en la tabla
