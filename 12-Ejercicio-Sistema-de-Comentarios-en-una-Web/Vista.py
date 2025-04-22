import Controller as ctr



print("Bienvenido al sistema de gestion de productos")
flag = True

while flag:
    try:
        print("Para ingresar un comentario presione 1")
        print("Para Consultar los comentarios de un usuario presione 2")
        print("Para consultar los usuarios presione 3")
        print("Para actializar un comentario presione 4")
        print("Para eliminar un comentario presione 5")
        print("Para salir del programa presione 6")
        opc = int(input("Digite la opcion: "))


        if opc == 1:
            print("Agregar Comentario")
            ctr.agregarComentario()
        elif opc == 2:
            print("consultar comentarios por usuario")
            ctr.consultarComentariosUsuario()
        elif opc == 3:
            print("Consultar los usuarios")
            ctr.consultarUsuarios()
        elif opc == 4:
            print("Actualizar comentario")
            ctr.actualizarComentario()
        elif opc == 5:
            print("Eliminar comentario")
            ctr.eliminarComentario()
        elif opc == 6:
            print("Gracias por usar el sistema")
            flag = False
            break

    except ValueError:
        print("Error, solo se permiten numeros enteros")
        continue