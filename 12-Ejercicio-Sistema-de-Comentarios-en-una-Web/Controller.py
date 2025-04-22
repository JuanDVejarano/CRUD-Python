import sqlite3 as db
from prettytable import PrettyTable

def consultarUsuarios():
    conn = db.connect("Comentarios.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Usuario"
    resultado = cursor.execute(instruccionSQL)
    for dato in resultado:
        print("""
                ID: {}
                Nombre: {}
                Email: {}
                """.format(dato[0], dato[1], dato[2]))
    conn.close()


def validarUsuario(idf):
    conn = db.connect("Comentarios.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Usuario WHERE idUsuario = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True
    
def validarComentario(idf):
    conn = db.connect("Comentarios.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT * FROM Comentario WHERE idComentario = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    if resultado.fetchone() is not None:
        conn.close()
        return False
    else:
        conn.close()
        return True

def agregarComentario():
    idUser = int(input("Digite el id del usuario: "))
    if (len(str(idUser)) == 0):
        print("Error, no se permiten campos vacios")
        print("Verifique que los datos sean correctos")
        return
    if (validarUsuario(idUser)):
        print("El ID no existe en la base de datos")
        return
    cometario = input("Digite el comentario: ")

    #controlar contenido datos
    if (len(cometario) > 0):
        conn = db.connect("Comentarios.db")
        cursor = conn.cursor()
        instruccionSQL = "INSERT INTO Comentario (idUsuario, comentario) VALUES (?, ?)"
        cursor.execute(instruccionSQL, (idUser, cometario))
        conn.commit()
        conn.close()
        print("El registro se creo exitosamente")
    else:
        print("Error, no se permiten campos vacios")
        print("Verifique que los datos sean correctos")

def consultarComentariosUsuario():
    idf = int(input("Digite el ID del usuario a consultar: "))
    if (validarUsuario(idf)):
        print("El ID no existe en la base de datos")
        return
    conn = db.connect("Comentarios.db")
    cursor = conn.cursor()
    instruccionSQL = "SELECT C.idComentario, C.comentario, U.nombre FROM Comentario C inner join Usuario U on C.idUsuario = U.idUsuario WHERE U.idUsuario = ?"
    resultado = cursor.execute(instruccionSQL, (idf,))
    for dato in resultado:
        print("""
                ID: {}
                Comentario: {}
                Usuario: {}
                """.format(dato[0], dato[1], dato[2]))
    conn.close()


def actualizarComentario():
    idf = int(input("Digite el ID del comentario a actualizar: "))
    if (validarComentario(idf)):
        print("El ID del comentario no existe en la base de datos")
        return
    cometario = input("Digite el nuevo comentario: ")
    if (len(cometario) > 0):
        conn = db.connect("Comentarios.db")
        cursor = conn.cursor()
        instruccionSQL = "UPDATE Comentario SET comentario = ? WHERE idComentario = ?"
        cursor.execute(instruccionSQL, (cometario, idf))
        conn.commit()
        conn.close()
        print("El registro se actualizo exitosamente")
    else:
        print("Error, no se permiten campos vacios")
        print("Verifique que los datos sean correctos")


def eliminarComentario():
    idf = int(input("Digite el ID del comentario a eliminar: "))
    if (validarComentario(idf)):
        print("El ID del comentario no existe en la base de datos")
        return
    conn = db.connect("Comentarios.db")
    cursor = conn.cursor()
    instruccionSQL = "DELETE FROM Comentario WHERE idComentario = ?"
    cursor.execute(instruccionSQL, (idf,))
    conn.commit()
    conn.close()
    print("El registro se elimino exitosamente")

