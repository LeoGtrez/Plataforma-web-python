import db
from sqlalchemy import Column, Integer, String, Boolean

class Users(db.Base): #Definimos clase Users
    __tablename__ = "users" #La clase se asocia con la tabla "users" en la base de datos
    #Se definen los atributos:
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    nombre = Column(String(200), nullable=False)
    psswd = Column(String, nullable=False)
    admin = Column(Boolean)
    vistas_movies = Column(String)
    vistas_shows = Column(String)
    favoritas_movies = Column(String)
    favoritas_shows = Column(String)

    #Se define la función "constructor"
    def __init__(self, nombre, psswd, admin, vistas_movies, vistas_shows, favoritas_movies, favoritas_shows):
        self.nombre = nombre
        self.psswd = psswd
        self.admin = admin
        self.vistas_movies = vistas_movies
        self.vistas_shows = vistas_shows
        self.favoritas_movies = favoritas_movies
        self.favoritas_shows = favoritas_shows

    #Se define la función "__str__"
    def __str__(self):
        return "User({}: {})".format(self.id, self.nombre)

class Movies(db.Base): #Definimos la clase Movies
    __tablename__ = "movies" #La clase se asocia con la tabla "movies" en la base de datos
    #Se definen los atributos:
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    title = Column(String, nullable=False)
    year = Column(Integer)
    #synopsis = Column(String, nullable=False)
    #rating = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    director = Column(String, nullable=False)
    runtime = Column(String, nullable=False)
    link = Column(String, nullable=False)

    # Se define la función "constructor"
    def __init__(self, title, year, genre, director, runtime, link):
        self.title = title
        self.year = year
        #self.synopsis = synopsis
        #self.rating = rating
        self.genre = genre
        self.director = director
        self.runtime = runtime
        self.link = link

    # Se define la función "__str__"
    def __str__(self):
        return "Movie({}: {}, {})".format(self.id, self.title, self.year)

class Shows(db.Base): #Definimos la clase Shows
    __tablename__ = "shows" #La clase se asocia con la tabla "shows" en la base de datos
    #Se definen los atributos:
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    title = Column(String, nullable=False)
    #synopsis = Column(String, nullable=False)
    year = Column(Integer)
    runtime = Column(Integer)
    genre = Column(String, nullable=False)
    seasons = Column(Integer)
    link = Column(String, nullable=False)

    # Se define la función "constructor"
    def __init__(self, title, year, runtime, genre, seasons, link):
        self.title = title
        #self.synopsis = synopsis
        self.year = year
        self.runtime = runtime
        self.genre = genre
        self.seasons = seasons
        self.link = link

    # Se define la función "__str__"
    def __str__(self):
        return "Show({}: {}, {})".format(self.id, self.title, self.year)