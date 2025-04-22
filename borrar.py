def ValidarNombre(nombre):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Producto WHERE nombre = ?"
    resultado = cursor.execute(instruccionSQL, (nombre,))
    print(resultado.fetchone())
    if resultado.fetchone() is not None:
        print("El nombre del producto ya existe")
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def ValidarCategoria(categoria):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM categoria WHERE id = ?"
    resultado = cursor.execute(instruccionSQL, (categoria,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True

def validarIdPrducto(idf):
    conn = db.connect("Inventario.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Producto WHERE id = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True
