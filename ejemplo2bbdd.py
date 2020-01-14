import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(20),
    PRECIO INTEGER,
    SECCION VARCHAR(20)
    )
''')

productos=[
    ("PELOTA",20,"JUGUETERIA"),
    ("PANTALON",20,"ROPA"),
    ("DESTORNILLADOR",20,"FERRETERIA"),
    ("JARRÓN",20,"CERAMICA")            
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()

miConexion.close()