select c.nombreCliente,fte.pedido,fte.etiqueta,fte.fecha,m.codigo
"Codigo Material",m.nombre "Nombre Material",mal.tipo "Tipo Malla",
mal.int_o_ext "Interno/Externo", t.color "Color Tinta", t.tipo "Tipo Tinta",
t.anilox "Anilox Tinta", t.proveedor "Proveedor 1", t.proveedor2 "Proveedor 2",
t.proveedor3 "Proveedor 3 "
from practica.cliente as c
join practica.ficha_tecnica_etiqueta as fte
on(c.idCliente = fte.idCliente)
left join practica.material_ficha as mf 
on(fte.idFicha = mf.idFicha)
left join practica.material as m
on(mf.idMaterial = m.idMaterial)
left join practica.malla_ficha as malf
on(malf.idFicha = fte.idFicha)
left join practica.malla as mal
on (malf.idMalla = mal.idMalla)
left join practica.tinta_ficha as tf
on (tf.idFicha = fte.idFicha)
left join practica.tinta as t
on (t.idTinta = tf.idTinta);