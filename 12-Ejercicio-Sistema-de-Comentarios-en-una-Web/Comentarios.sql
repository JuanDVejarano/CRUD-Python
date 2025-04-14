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