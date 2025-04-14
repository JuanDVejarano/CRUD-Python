Create Table Usuario
(
    idUsuario Integer PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

Create Table Comentario
(
    idComentario Integer PRIMARY KEY AUTOINCREMENT,
    idUsuario Integer NOT NULL,
    comentario TEXT NOT NULL,
    fecha TEXT DEFAULT CURRENT_DATE,
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);

INSERT INTO Usuario (nombre, email)
VALUES ('Juan Perez', 'juan.perez@example.com'),
       ('Maria Lopez', 'maria.lopez@example.com'),
       ('Carlos Gomez', 'carlos.gomez@example.com'),
       ('Estiven Galindo', 'estiven.galindo@example.com');


INSERT INTO Comentario (idUsuario, comentario)
VALUES 
    (1, 'Este es un comentario de Juan Perez.'),
    (2, 'Este es un comentario de Maria Lopez.'),
    (3, 'Este es un comentario de Carlos Gomez.'),
    (4, 'Este es un comentario de Estiven Galindo.'),
    (1, 'Otro comentario de Juan Perez.'),
    (2, 'Otro comentario de Maria Lopez.'),
    (3, 'Un comentario adicional de Carlos Gomez.'),
    (4, 'Un comentario adicional de Estiven Galindo.'),
    (1, 'Un tercer comentario de Juan Perez.'),
    (2, 'Un tercer comentario de Maria Lopez.'),
    (3, 'Carlos Gomez tiene algo más que decir.'),
    (4, 'Estiven Galindo también tiene algo más que decir.'),
    (1, 'Juan Perez sigue comentando.'),
    (2, 'Maria Lopez sigue comentando.'),
    (3, 'Carlos Gomez no se queda atrás.'),
    (4, 'Estiven Galindo tampoco se queda atrás.'),
    (1, 'Juan Perez tiene otro comentario interesante.'),
    (2, 'Maria Lopez comparte otro comentario.'),
    (3, 'Carlos Gomez agrega un nuevo comentario.'),
        (4, 'Estiven Galindo cierra con este comentario.');