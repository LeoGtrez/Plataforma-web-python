import db
import csv
import os
from flask import Flask, render_template, request, redirect, url_for
from models import Users, Movies, Shows

app = Flask(__name__) #Creamos objeto Flask

@app.route("/") #Definimos el punto de partida de la web (index.html) en el que le pedimos nombre
                # y contraseña al usuario para iniciar la sesión
def home():
    return render_template("index.html")

@app.route("/main", methods=["GET","POST"]) #Verificación de nombre de usuario y contraseña
def main(): #Función para discernir que tanto la contraseña como el nombre de usuario son correctos
    global nombre_login
    nombre_login = request.form["nombre-usuario"]#Definimos nombre_login como variable global para acceder a
    # la info del usuario en cualquier punto del programa
    existe_nombre = db.session.query(Users).filter_by(nombre=nombre_login).first() is not None
    existe_psswd = db.session.query(Users).filter_by(psswd=request.form["password"]).first() is not None
    if existe_nombre and existe_psswd: #Si es correcto redirigimos a la primera página del catálogo de peliculas.
        return redirect(url_for("pelis1"))
    else: #Si no están bien introducidas, redirigimos otra vez a la página de inicio mostrando un mensaje.
        msg="Nombre de usuario o contraseña incorrectos, prueba otra vez"
        return render_template("index.html",message=msg)

@app.route("/peliculas1", methods=["GET"]) #Primera página del catálogo de películas
def pelis1():
    _50_pelis_1 = db.session.query(Movies).filter(Movies.id < 101) #Buscamos las primeras 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis = _50_pelis_1,pg=1,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas2", methods=["GET"]) #Segunda página del catálogo de películas
def pelis2():
    _50_pelis_2 = db.session.query(Movies).filter(Movies.id > 100, Movies.id < 201)#Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis = _50_pelis_2,pg=2,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas3", methods=["GET"]) #Tercera página del catálogo de películas
def pelis3():
    _50_pelis_3 = db.session.query(Movies).filter(Movies.id > 200, Movies.id < 301) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_3,pg=3,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas4", methods=["GET"]) #Cuarta página del catálogo de películas
def pelis4():
    _50_pelis_4 = db.session.query(Movies).filter(Movies.id > 300, Movies.id < 401) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_4,pg=4,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas5", methods=["GET"]) #Quinta página del catálogo de películas
def pelis5():
    _50_pelis_5 = db.session.query(Movies).filter(Movies.id > 400, Movies.id < 501) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_5,pg=5,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas6", methods=["GET"]) #Sexta página del catálogo de películas
def pelis6():
    _50_pelis_6 = db.session.query(Movies).filter(Movies.id > 500, Movies.id < 601) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_6,pg=6,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas7", methods=["GET"]) #Séptima página del catálogo de películas
def pelis7():
    _50_pelis_7 = db.session.query(Movies).filter(Movies.id > 600, Movies.id < 701) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_7,pg=7,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas8", methods=["GET"]) #Octava página del catálogo de películas
def pelis8():
    _50_pelis_8 = db.session.query(Movies).filter(Movies.id > 700, Movies.id < 801) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_8,pg=8,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas9", methods=["GET"]) #Novena página del catálogo de películas
def pelis9():
    _50_pelis_9 = db.session.query(Movies).filter(Movies.id > 800, Movies.id < 901) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_9,pg=9,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/peliculas10", methods=["GET"]) #Décima página del catálogo de películas
def pelis10():
    _50_pelis_10 = db.session.query(Movies).filter(Movies.id > 900, Movies.id < 1001) #Buscamos las siguientes 100 películas de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_movies_int = [] # Inicialización lista
    id_movies_fav = [] # Inicialización lista

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == '': #Si no hay películas favoritass para el usuario la lista se deja vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
    return render_template("main_home.html", lista_de_pelis=_50_pelis_10,pg=10,id_int=id_movies_int,
                           id_fav=id_movies_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series1", methods=["GET"]) #Primera página del catálogo de series
def series1():
    serieslst_1 = db.session.query(Shows).filter(Shows.id < 51) #Buscamos las primeras 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_1,pg=1,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series2", methods=["GET"]) #Segunda página del catálogo de series
def series2():
    serieslst_2 = db.session.query(Shows).filter(Shows.id > 50, Shows.id < 101) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_2,pg=2,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series3", methods=["GET"]) #Tercera página del catálogo de series
def series3():
    serieslst_3 = db.session.query(Shows).filter(Shows.id > 100, Shows.id < 151) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_3,pg=3,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series4", methods=["GET"]) #Cuarta página del catálogo de series
def series4():
    serieslst_4 = db.session.query(Shows).filter(Shows.id > 150, Shows.id < 201) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_4,pg=4,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series5", methods=["GET"]) #Quinta página del catálogo de series
def series5():
    serieslst_5 = db.session.query(Shows).filter(Shows.id > 200, Shows.id < 251) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_5,pg=5,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series6", methods=["GET"]) #Sexta página del catálogo de series
def series6():
    serieslst_6 = db.session.query(Shows).filter(Shows.id > 250, Shows.id < 301) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_6,pg=6,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series7", methods=["GET"]) #Séptima página del catálogo de series
def series7():
    serieslst_7 = db.session.query(Shows).filter(Shows.id > 300, Shows.id < 351) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_7,pg=7,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/series8", methods=["GET"]) #Octava página del catálogo de series
def series8():
    serieslst_8 = db.session.query(Shows).filter(Shows.id > 350) #Buscamos las siguientes 50 series de la base de datos
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)
    id_shows_int = [] # Inicialización lista
    id_shows_fav = [] # Inicialización lista

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
    return render_template("main_series.html", lista_de_series=serieslst_8,pg=8,id_int=id_shows_int,
                           id_fav=id_shows_fav, admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/vistas", methods=["GET"]) #Página para mostrar el catálogo de películas y series vistas
def vistas():
    vistas_pelis_lst = [] # Inicialización lista
    vistas_shows_lst = [] # Inicialización lista
    id_movies_int = []  # Inicialización lista
    id_shows_int = []  # Inicialización lista
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (un objeto Users)

    if user.vistas_movies == '': #Si no hay películas vistas para el usuario la lista se deja vacía
        id_movies_int = []
        vistas_pelis_lst = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))
        for i in range(len(id_movies_lst)): #Para cada elemento de la lista se busca el objeto "Movie" asociado
            # y se guarda en una lista
            vistas_pelis_lst.append(db.session.query(Movies).filter_by(id=int(id_movies_lst[i])).first())

    if user.vistas_shows == '': #Si no hay series vistas para el usuario la lista se deja vacía
        id_shows_int = []
        vistas_shows_lst = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))
        for i in range(len(id_shows_lst)):#Para cada elemento de la lista se busca el objeto "Show" asociado
            # y se guarda en una lista
            vistas_shows_lst.append(db.session.query(Shows).filter_by(id=int(id_shows_lst[i])).first())

    return render_template("vistas.html", pelis_vistas=vistas_pelis_lst, series_vistas=vistas_shows_lst,
                           id_movies=id_movies_int, id_shows=id_shows_int, admin=user.admin) #Se carga plantilla HTML
    # y se envían parámetros/variables

@app.route("/pelicula-vista/<id>") #Función para marcar una película como "vista"
def pelicula_vista(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    if user.vistas_movies == "": #Si no hay películas vistas para el usuario se modifica directamente atributo .vistas_movies
        user.vistas_movies = str(id)
    else: #En caso contrario, se crea lista con split() y se añade ("append") el nuevo "id" de película
        id_movies_lst = str(user.vistas_movies).split(",")
        id_movies_lst.append(str(id))
        user.vistas_movies = ",".join(id_movies_lst) #Se guarda string en atributo .vistas_movies
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/pelicula-no-vista/<id>") #Función para marcar una película como "no vista"
def pelicula_no_vista(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    id_movies_lst = str(user.vistas_movies).split(",") #Se crea lista con split()
    index = id_movies_lst.index(str(id)) #Se averigua el índice que tiene asociado el "id" de la película
    id_movies_lst.pop(index) #Se elimina de la lista una vez se sabe el numero de índice
    user.vistas_movies = ",".join(id_movies_lst) #Se guarda string en atributo .vistas_movies
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/serie-vista/<id>") #Función para marcar una serie como "vista"
def serie_vista(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    if user.vistas_shows == "": #Si no hay series vistas para el usuario se modifica directamente atributo .vistas_shows
        user.vistas_shows = str(id)
    else: #En caso contrario, se crea lista con split() y se añade ("append") el nuevo "id" de la serie
        id_shows_lst = str(user.vistas_shows).split(",")
        id_shows_lst.append(str(id))
        user.vistas_shows = ",".join(id_shows_lst) #Se guarda string en atributo .vistas_shows
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/serie-no-vista/<id>") #Función para marcar una serie como "no vista"
def serie_no_vista(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    id_shows_lst = str(user.vistas_shows).split(",") #Se crea lista con split()
    index = id_shows_lst.index(str(id)) #Se averigua el índice que tiene asociado el "id" de la serie
    id_shows_lst.pop(index) #Se elimina de la lista una vez se sabe el numero de índice
    user.vistas_shows = ",".join(id_shows_lst) #Se guarda string en atributo .vistas_shows
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/favoritas") #Página para mostrar el catálogo de películas y series favoritas
def favoritas():
    fav_pelis_lst = [] # Inicialización lista
    fav_shows_lst = [] # Inicialización lista
    id_movies_fav = []  # Inicialización lista películas favoritas
    id_shows_fav = [] # Inicialización lista series favoritas
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)

    if user.favoritas_movies == '': #Si no hay películas favoritas para el usuario la lista se deja vacía
        id_movies_fav = []
        fav_pelis_lst = []
    else:
        id_movies_lst = str(user.favoritas_movies).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))
        for i in range(len(id_movies_lst)):#Para cada elemento de la lista se busca el objeto "Movie" asociado
            # y se guarda en una lista
            fav_pelis_lst.append(db.session.query(Movies).filter_by(id=int(id_movies_lst[i])).first())

    if user.favoritas_shows == '': #Si no hay series favoritas para el usuario la lista se deja vacía
        id_shows_fav = []
        fav_shows_lst = []
    else:
        id_shows_lst = str(user.favoritas_shows).split(",") #En caso contrario, se crea una lista a partir de split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))
        for i in range(len(id_shows_lst)):#Para cada elemento de la lista se busca el objeto "Show" asociado
            # y se guarda en una lista
            fav_shows_lst.append(db.session.query(Shows).filter_by(id=int(id_shows_lst[i])).first())

    return render_template("favoritas.html", pelis_fav=fav_pelis_lst, series_fav=fav_shows_lst,
                           id_movies=id_movies_fav, id_shows=id_shows_fav, admin=user.admin) #Se carga plantilla HTML
    # y se envían parámetros/variables

@app.route("/pelicula-fav/<id>") #Función para marcar una película como "favorita"
def pelicula_fav(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    if user.favoritas_movies == "": #Si no hay películas vistas para el usuario se modifica directamente atributo .favoritas_movies
        user.favoritas_movies = str(id)
    else: #En caso contrario, se crea lista con split() y se añade ("append") el nuevo "id" de película
        id_movies_lst = str(user.favoritas_movies).split(",")
        id_movies_lst.append(str(id))
        user.favoritas_movies = ",".join(id_movies_lst) #Se guarda string en atributo .favoritas_movies
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/pelicula-no-fav/<id>") #Función para marcar una película como "no favorita"
def pelicula_no_fav(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    id_movies_lst = str(user.favoritas_movies).split(",") #Se crea lista con split()
    index = id_movies_lst.index(str(id)) #Se averigua el índice que tiene asociado el "id" de la película
    id_movies_lst.pop(index) #Se elimina de la lista una vez se sabe el numero de índice
    user.favoritas_movies = ",".join(id_movies_lst) #Se guarda string en atributo .favoritas_movies
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/serie-fav/<id>") #Función para marcar una serie como "favorita"
def serie_fav(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    if user.favoritas_shows == "": #Si no hay series vistas para el usuario se modifica directamente atributo .favoritas_shows
        user.favoritas_shows = str(id)
    else: #En caso contrario, se crea lista con split() y se añade ("append") el nuevo "id" de la serie
        id_shows_lst = str(user.favoritas_shows).split(",")
        id_shows_lst.append(str(id))
        user.favoritas_shows = ",".join(id_shows_lst) #Se guarda string en atributo .favoritas_shows
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/serie-no-fav/<id>") #Función para marcar una serie como "no favorita"
def serie_no_fav(id):
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario (objeto Users)
    id_shows_lst = str(user.favoritas_shows).split(",") #Se crea lista con split()
    index = id_shows_lst.index(str(id)) #Se averigua el índice que tiene asociado el "id" de la serie
    id_shows_lst.pop(index) #Se elimina de la lista una vez se sabe el numero de índice
    user.favoritas_shows = ",".join(id_shows_lst) #Se guarda string en atributo .favoritas_shows
    db.session.flush()
    db.session.commit() #Se guardan los cambios en base de datos
    return redirect(request.referrer) #Se redirige a la página anterior

@app.route("/search",methods=["POST"]) #Página que muestra las películas y series cuyos títulos coinciden con las palabras
# introducidas en el buscador
def buscadas():
    search_word = request.form["search"] #Se asigna la palabra introducida en el "input" a una variable
    search_pelis_lst = db.session.query(Movies).filter(Movies.title.contains(search_word)).all() #Todas las películas cuyos
    #títulos contienen la palabra buscada
    search_shows_lst = db.session.query(Shows).filter(Shows.title.contains(search_word)).all() #Todas las series cuyos
    #títulos contienen la palabra buscada
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Datos del usuario [Objeto Users)

    id_movies_int = [] #Inicicalización lista
    id_movies_fav = [] #Inicialización lista
    if user.vistas_movies == "": #Si no hay películas vistas para el ususario se deja la lista vacía
        id_movies_int = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #En caso contrarío, se crea una lista con split()
        for el in id_movies_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_int.append(int(el))

    if user.favoritas_movies == "": #Si no hay películas favoritas para el ususario se deja la lista vacía
        id_movies_fav = []
    else:
        id_movies_favlst = str(user.favoritas_movies).split(",") #En caso contrarío, se crea una lista con split()
        for el in id_movies_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_movies_fav.append(int(el))

    id_shows_int = [] #Inicicalización lista
    id_shows_fav = [] #Inicicalización lista
    if user.vistas_shows == "":  #Si no hay series vistas para el ususario se deja la lista vacía
        id_shows_int = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #En caso contrarío, se crea una lista con split()
        for el in id_shows_lst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_int.append(int(el))

    if user.favoritas_shows == "": #Si no hay series favoritas para el ususario se deja la lista vacía
        id_shows_fav = []
    else:
        id_shows_favlst = str(user.favoritas_shows).split(",") #En caso contrarío, se crea una lista con split()
        for el in id_shows_favlst: #Cada elemento en la lista se guarda en otra lista como integer
            id_shows_fav.append(int(el))

    return render_template("buscadas.html", srch_w=search_word, pelis_buscadas=search_pelis_lst,
                           series_buscadas=search_shows_lst, id_movies_v=id_movies_int,
                           id_movies_f=id_movies_fav, id_shows_v=id_shows_int, id_shows_f=id_shows_fav,
                           admin=user.admin) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/admin") #Página de administrador
def admin():
    users = db.session.query(Users).all() #Definimos lista de usuarios (objetos Users)
    movies_count_lst = [] # Inicialización lista
    shows_count_lst = [] #Inicialización lista

    for user in users: #Bucle para cada usuario
        if user.vistas_movies == "": #Si no hay películas vistas por el usuario, se añade un 0 en la lista
            movies_count_lst.append(0)
        else:
            id_movies_lst = str(user.vistas_movies).split(",") #Se crea lista de "id's" de películas vistas, con split()
            movies_count_lst.append(len(id_movies_lst)) #Se cuentan el nº de "id's" y se añaden a la lista "movies_count_lst"

        if user.vistas_shows == "": #Si no hay series vistas por el usuario, se añade un 0 en la lista
            shows_count_lst.append(0)
        else:
            id_shows_lst = str(user.vistas_shows).split(",") #Se crea lista de "id's" de series vistas, con split()
            shows_count_lst.append(len(id_shows_lst)) #Se cuentan el nº de "id's" y se añaden a la lista "shows_count_lst"

    return render_template("admin.html", lista_usuarios=users, movies_count=movies_count_lst,
                           shows_count=shows_count_lst, edit=False) #Se carga plantilla HTML y se envían parámetros/variables

@app.route("/crear-usuario", methods=["POST"]) #Función para crear nuevo usuario a partir de parámetros de formulario <form>
def create_user():
    if request.form["permisos"] == "admin": #Se añaden permisos de administrador en función de los elegido en el formulario
        admin_bool = True
    else:
        admin_bool = False
    user = Users(nombre=request.form["nombre-user"], psswd=request.form["password"], admin=admin_bool,
                 vistas_movies="", vistas_shows="",
                 favoritas_movies="", favoritas_shows="") #Se crea el objeto Users con los parámetros / variables del
    # formulario y las listas de vistas/favoritas se generan vacías por defecto
    db.session.add(user) #Se añade objeto a la base de datos
    db.session.commit() #Se guardan los cambios en la base de datos
    return redirect(url_for("admin")) #Se redirige a la página de administrador

@app.route("/cargar-usuario/<id>", methods=["GET","POST"]) #Función para cargar información del usuario para editarla luego
def load_user(id):
    users = db.session.query(Users).all() #Definimos lista de usuarios (objetos Users)
    user = db.session.query(Users).filter_by(id=id).first() #Buscamos el usuario que coincida con el "id"
    movies_count_lst = [] #Inicialización de lista
    shows_count_lst = [] #Inicialización de lista

    for el in users: #Bucle para cada usuario
        if el.vistas_movies == "": #Si no hay películas vistas por el usuario, se añade un 0 en la lista
            movies_count_lst.append(0)
        else:
            id_movies_lst = str(el.vistas_movies).split(",") #Se crea lista de "id's" de películas vistas, con split()
            movies_count_lst.append(len(id_movies_lst)) #Se cuentan el nº de "id's" y se añaden a la lista "movies_count_lst"

        if el.vistas_shows == "": #Si no hay series vistas por el usuario, se añade un 0 en la lista
            shows_count_lst.append(0)
        else:
            id_shows_lst = str(el.vistas_shows).split(",") #Se crea lista de "id's" de series vistas, con split()
            shows_count_lst.append(len(id_shows_lst)) #Se cuentan el nº de "id's" y se añaden a la lista "shows_count_lst"
    return render_template("admin.html", lista_usuarios=users, movies_count=movies_count_lst,
                           shows_count=shows_count_lst, user_to_edit=user, edit=True) #Se carga plantilla HTML y se
    # envían parámetros/variables

@app.route("/editar-usuario/<id>", methods=["GET","POST"]) #Función para editar la información del usuario elegido
def edit_user(id):
    user_to_edit = db.session.query(Users).filter_by(id=id).first() #Buscamos el usuario que coincida con el "id"
    if request.form["permisos"] == "admin": #Se añaden permisos de administrador en función de los elegido en el formulario
        admin_bool = True
    else:
        admin_bool = False
    user_to_edit.nombre=request.form["nombre-user"] #Se asigna el nombre de usuario nuevo en función del "input"
    user_to_edit.psswd=request.form["password"] #Se asigna la nueva contraseña en función del "input"
    user_to_edit.admin=admin_bool #Se asigna la variable admin "booleana"
    db.session.commit() #Se guardan los cambios en la base de datos
    return redirect(url_for("admin")) #Se redirige a la página de administrador

@app.route("/eliminar-usuario/<id>", methods=["GET"]) #Función para eliminar el usuario elegido
def delete_user(id):
    userdel = db.session.query(Users).filter_by(id=id) #Buscamos el usuario que coincida con el "id"
    userdel.delete() #Se elmina el usuario de la base de datos
    db.session.commit() #Se guardan los cambios en la base de datos
    return redirect(url_for("admin")) #Se redirige a la página de administrador

@app.route("/catalogo_pelis") #Página de administrador para el catálogo de películas
def admin_pelis():
    pelis = db.session.query(Movies).all() #Definimos la lista de películas (todas)
    return render_template("admin_pelis.html", lista_movies=pelis, edit=False) #Se carga plantila HTML y se
    # envían los parámetros / variables

@app.route("/crear-peli", methods=["POST"]) #Función para crear registro nuevo de Película
def create_movie():
    time=request.form["runtime_h"]+"h "+request.form["runtime_min"]+"m" #Se define la variable en donde se guarda el "runtime"
    movie = Movies(title=request.form["title"], year=request.form["year"], genre=request.form["genre"],
                  director=request.form["director"], runtime=time, link=request.form["link"]) #Se crea nuevo objeto "Movies"
    db.session.add(movie) #Se añade el objeto "Movie" en la base de datos
    db.session.commit() #Se guardan los cambios en la base de datos
    return redirect(url_for("admin_pelis")) #Se redirige a la página de administrador para el catálogo de películas

@app.route("/cargar-peli/<id>", methods=["GET","POST"]) #Función para cargar el registro de película que se quiere editar
def load_movie(id):
    pelis = db.session.query(Movies).all() #Se define la lista de películas (todas)
    movie = db.session.query(Movies).filter_by(id=id).first() #Buscamos la película que coincide con el "id" elegido
    runtime_lst=movie.runtime.split(" ") #Variable para poder separar horas y minutos
    if len(runtime_lst) == 1: #Se separan horas y minutos, teniendo en cuenta que hay casos en donde hay "0" minutos
        runtime_h = runtime_lst[0].translate({ord(i): None for i in "h'"})
        runtime_min = "0"
    else:
        runtime_h=runtime_lst[0].translate({ord(i): None for i in "h'"})
        runtime_min=runtime_lst[1].translate({ord(i): None for i in "m'"})
    return render_template("admin_pelis.html", lista_movies=pelis, movie_to_edit=movie,
                           time_h=runtime_h, time_m=runtime_min, edit=True) #Se carga plantilla HTML y se envían
    # parámetros / variables

@app.route("/editar-peli/<id>", methods=["GET","POST"]) #Función para editar el registro de película elegido
def edit_movie(id):
    movie_to_edit = db.session.query(Movies).filter_by(id=id).first() #Se busca el registro de película que coincide con el "id"
    movie_to_edit.title = request.form["title"] #Se asigna "título" nuevo al registro
    movie_to_edit.year = request.form["year"] #Se asigna "año de lanzamiento" nuevo al registro
    movie_to_edit.genre = request.form["genre"] #Se asigna "géneros" nuevos al registro
    movie_to_edit.director = request.form["director"] #Se asigna "director" nuevo al registro
    movie_to_edit.runtime = request.form["runtime_h"]+"h "+request.form["runtime_min"]+"m" #Se asigna nuevo "runtime"
    movie_to_edit.link = request.form["link"] #Se asigna nuevo link de póster de película
    db.session.commit() #Guardamos cambios en la base de datos
    return redirect(url_for("admin_pelis")) #Se redirige a la página de administracíon del catálogo de Películas

@app.route("/eliminar-peli/<id>", methods=["GET"]) #Función para eliminar el registro de película elegida
def delete_movie(id):
    moviedel = db.session.query(Movies).filter_by(id=id) #Se busca el registro de película que coincide con el "id"
    moviedel.delete() #Se elimina registro de la base de datos
    db.session.commit() #Se guarda el cambio hecho en la base de datos
    return redirect(url_for("admin_pelis")) #Se redirige a la página de administracíon del catálogo de Películas

@app.route("/catalogo_series") #Página de administrador para el catálogo de Series
def admin_series():
    series = db.session.query(Shows).all() #Se define lista de series (todas)
    return render_template("admin_series.html", lista_series=series, edit=False) #Se carga plantilla HTML y se
    # envían parámetros / variables

@app.route("/crear-serie", methods=["POST"]) #Funcion para crear registro de serie nuevo
def create_show():
    #Se crea objeto "Shows" nuevo con información del formulario
    show = Shows(title=request.form["title"], year=request.form["year"],  runtime=request.form["runtime_min"],
                 genre=request.form["genre"], seasons=request.form["seasons"], link=request.form["link"])
    db.session.add(show) #Se añade el nuevo objeto a la base de datos
    db.session.commit() #Guardamos cambio realizado en la base de datos
    return redirect(url_for("admin_series")) #Se redirige a la página de administrador para el catálogo de Series

@app.route("/cargar-serie/<id>", methods=["GET","POST"]) #Función para cargar el registro de serie que se quiere editar
def load_show(id):
    series = db.session.query(Shows).all() #Se define lista de Series (todas)
    show = db.session.query(Shows).filter_by(id=id).first() #Se busca registro de Serie que coincide con el "id"

    return render_template("admin_series.html", lista_series=series, show_to_edit=show, edit=True) #Se carga plantilla HTML
    # y se envían parámetros / variables

@app.route("/editar-serie/<id>", methods=["GET","POST"]) #Función para editar el registro elegido
def edit_show(id):
    show_to_edit = db.session.query(Shows).filter_by(id=id).first() #Se busca registro de serie que coincide con "id"
    show_to_edit.title = request.form["title"] #Se asigna nuevo "título" al registro
    show_to_edit.year = request.form["year"] #Se asigna nuevo "año de lanzamiento" al registro
    show_to_edit.runtime = request.form["runtime_min"] #Se asigna nuevo "runtime" al registro
    show_to_edit.genre = request.form["genre"] #Se asigna nuevos "géneros" al registro
    show_to_edit.seasons = request.form["seasons"] #Se asigna el "nº de temporadas" nuevo al registro
    show_to_edit.link = request.form["link"] #Se asigna el link nuevo
    db.session.commit() #Guardamos cambios realizados en la base de datos
    return redirect(url_for("admin_series")) #Redirigimos a la página de administrador (catálogo de Series)

@app.route("/eliminar-serie/<id>", methods=["GET"]) #Función para eliminar el registro elegido
def delete_show(id):
    showdel = db.session.query(Shows).filter_by(id=id) #Se busca registro de serie que coincide con "id"
    showdel.delete() #Se elimina el registro de la base de datos
    db.session.commit() #Guardamos el cambio en la base de datos
    return redirect(url_for("admin_series")) #Se redirige a la página de administrador (catálogo de Series)

@app.route("/user_page", methods=["POST"]) #Página de usuario (info y resumen de actividad)
def user_page():
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Buscamos información de usuario (objeto Users)
    if user.vistas_movies == "": #Si no hay películas vistas por el usuario se asigna un 0 en el contador y se deja la lista vacia
        movies_count = 0
        id_movies_lst = []
    else:
        id_movies_lst = str(user.vistas_movies).split(",") #Se crea lista de películas vistas con split()
        movies_count = len(id_movies_lst) #Se cuenta el nº de películas vistas

    if user.vistas_shows == "":  #Si no hay series vistas por el usuario se asigna un 0 en el contador y se de ja la lista vacía
        shows_count = 0
        id_shows_lst = []
    else:
        id_shows_lst = str(user.vistas_shows).split(",") #Se crea lista de series vistas con split()
        shows_count = len(id_shows_lst) #Se cuenta el nº de series vistas

    pelis_vistas = [] #Inicialización lista
    for i in range(len(id_movies_lst)): #Se crea lista de películas (objetos Movies) vistas
        pelis_vistas.append(db.session.query(Movies).filter_by(id=int(id_movies_lst[i])).first())

    series_vistas = [] #Inicialización lista
    for i in range(len(id_shows_lst)): #Se crea lista de series (objetos Shows) vistas
        series_vistas.append(db.session.query(Shows).filter_by(id=int(id_shows_lst[i])).first())

    genre_sum = [] #Inicialización de lista
    for mv in pelis_vistas: #Para cada película vista
        genre_sum = genre_sum + mv.genre.split(",") #Se genera una lista de géneros de todas las películas vistas
    for sh in series_vistas: #Para cada series vista
        genre_sum = genre_sum + sh.genre.split(",") #Se añaden a la lista de géneros, los géneros de las series vistas

    for i in range(len(genre_sum)): #Se estandarizan los nombres de géneros (se borran espacios)
        genre_sum[i]=genre_sum[i].translate({ord(i): None for i in " "})

    genre_set = list(set(genre_sum)) #Se crea un lista del conjunto asociado a la lista de géneros (géneros que no se repiten)
    genre_count = [] #Inicialización de lista (contador)
    for el in genre_set: #Para cada elemento en la lista "genre_set"
        genre_count.append(genre_sum.count(el)) #Se cuenta las apariciones de cada género y se añade el número a una lista

    # Se carga la plantilla HTML y se envían los parámetros / variables
    return render_template("user_page.html", user=user, movies_total=int(movies_count),
                           shows_total=int(shows_count), genres=genre_set, genres_count=genre_count, admin=user.admin)

@app.route("/change-password", methods=["POST"]) #Cambio de contraseña
def change_password():
    user = db.session.query(Users).filter_by(nombre=nombre_login).first() #Buscamos información de usuario
    user.psswd = request.form["new-password"] #Se asigna nueva contraseña
    db.session.commit() #Guardamos cambio en la base de datos
    return redirect(url_for("user_page")) #Redirigimos a la página de usuario


def inicializar_tablas_db():
    # Datos por defecto de la base de datos "users"
    nombres_usuarios = (("Elena1993!", "3l3Na3109!", False, "", "","",""),
                        ("Maur0Nito", "MAU93-11?", False, "11,13,893,738", "12,32,45","3,78","4,32"),
                        ("SmallBOY", "Dani3l_9012$", True, "", "","",""),
                        ("Periclos", "pep0-lore!#", False, "18", "45","90,32","45"))
    for i in nombres_usuarios:
        user = Users(nombre=i[0], psswd=i[1], admin=i[2], vistas_movies=i[3], vistas_shows=i[4],
                     favoritas_movies=i[5], favoritas_shows=i[6]) #Se crean objetos Users
        db.session.add(user) #Se añaden objetos Users a la base de datos
        db.session.commit() #Se guardan cambios (base de datos)

    # Datos por defecto de la base de datos "movies"
    # Creamos una lista para cada columna (en total 8 listas)
    title_lst = []
    year_lst = []
    genre_lst = []
    director_lst = []
    runtime_lst = []
    link_lst = []

    # Abrimos csv
    cwd = os.getcwd()
    with open(cwd+"/database/peliculas.csv", "r") as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:  # Bucle for para asignar cada valor a las listas
            title_lst.append(row[1])
            year_lst.append(row[2])
            genre_lst.append(row[11])
            director_lst.append(row[13])
            runtime_lst.append(row[19])

    with open(cwd+"/database/movie_links.csv", "r") as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:  # Bucle for para asignar cada valor a las listas
            link_lst.append(row[0])

    # Eliminamos 1er elemento de cada lista
    title_lst.pop(0)
    year_lst.pop(0)
    genre_lst.pop(0)
    director_lst.pop(0)
    runtime_lst.pop(0)
    link_lst.pop(0)

    set_titles = list(set(title_lst)) #Lista de títulos de películas (sin repetir)
    for i in range(len(title_lst)): #Se añaden Películas en la base de datos comprobando que no se repitan títulos
        if title_lst[i] in set_titles:
            movie = Movies(title=title_lst[i], year=year_lst[i],
                       genre=genre_lst[i], director=director_lst[i], runtime=runtime_lst[i], link=link_lst[i])
            db.session.add(movie) #Se añade Movie a la base de datos
            db.session.commit() #Guardamos cambio en la base de datos
            pos=set_titles.index(title_lst[i]) #Averiguamos nº de indice del título
            set_titles.pop(pos) #Eliminamos título de la lista (para no repetirlo)
        else:
            continue

    # Datos por defecto de la base de datos "shows"
    # Creamos una lista para cada columna (en total 7 listas)
    title_show_lst = []
    #synopsis_show_lst = []
    year_show_lst = []
    runtime_show_lst = []
    genre_show_lst = []
    seasons_show_lst = []
    link_show_lst = []

    # Abrimos csv
    with open(cwd+"/database/Shows.csv", "r") as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:  # Bucle for para asignar cada valor a las listas
            title_show_lst.append(row[0])
            #synopsis_show_lst.append(row[1])
            year_show_lst.append(row[2])
            runtime_show_lst.append(row[3])
            genre_show_lst.append(row[4].translate({ord(i): None for i in "[]'"}))
            seasons_show_lst.append(row[5])

    with open(cwd+"/database/shows_links.csv", "r") as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:  # Bucle for para asignar cada valor a las listas
            link_show_lst.append(row[0])

    # Eliminamos 1er elemento de cada lista
    title_show_lst.pop(0)
    #synopsis_show_lst.pop(0)
    year_show_lst.pop(0)
    runtime_show_lst.pop(0)
    genre_show_lst.pop(0)
    seasons_show_lst.pop(0)
    link_show_lst.pop(0)

    for i in range(len(title_show_lst)):
        show = Shows(title=title_show_lst[i], year=year_show_lst[i], runtime=runtime_show_lst[i],
                       genre=genre_show_lst[i], seasons=seasons_show_lst[i], link=link_show_lst[i]) #Se crea objeto Shows
        db.session.add(show) #Se añade objeto a la base de datos
        db.session.commit() #Guardamos cambio en la base de datos


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) #Inicialización de la base de datos
    todas_las_pelis = db.session.query(Movies).all() #Cargamos lista de Películas
    if len(todas_las_pelis)==0: #Si la lista de películas está vacia (base  de datos vacía también), inicializamos tablas
        inicializar_tablas_db()

    app.run(debug=True) #Ponemos en marcha objeto Flask (web)