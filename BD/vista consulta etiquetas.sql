create view  vInfoEtiqueta as 
select  cat.nombre "Categoria" ,c.NombreCliente "Cliente",f.pedido "Pedido",f.etiqueta "Etiqueta",m.codigo "Maquina"
from  practica.ficha_tecnica_etiqueta as f left join practica.cliente as c
on c.idCliente = f.idCliente
left join practica.categoria as cat
on f.idCategoria = cat.idCategoria
left join practica.maquina as m
on m.idMaquina = f.idMaquina ;

select * from vInfoEtiqueta;
INSERT INTO FICHA_TECNICA_ETIQUETA (pedido,etiqueta,fecha,clisses,idCategoria,idCliente,idMaquina) VALUES ('002','Bena black ale',STR_TO_DATE('10/07/2011','%d/%m/%Y'),True,-1,-1,-1)