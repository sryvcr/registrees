# API REST con Django-Rest-Framework para relacionar árboles al parque que pertenecen


#### Crear proyecto

```sh
$ mkdir trees_park_rest
$ cd trees_park_rest
$ virtualenv . -p python3
$ mkdir src
$ cd src
```

#### Aplicar requerimientos
```sh
$ source ../bin/activate
$ (trees_parks_rest) python -m pip install requirements.txt
```

#### Configurar base de datos
```sh
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg',
            'NAME': 'arboles_db',
            'USER': 'postgres',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}
```
 
### Crear proyecto y apps
En cada carpeta nueva que se crea en el project no olvidar el archivo __init__.py si no se crea
automaticamente, para que Django reconozca el directorio como parte del proyecto
```sh
$ (trees_parks_rest) cd src/
$ (trees_parks_rest) python ../bin/django-admin.py startproject registrees
$ (trees_parks_rest) cd registrees/
$ (trees_parks_rest) mkdir apps/
$ (trees_parks_rest) cd apps/
$ (trees_parks_rest) python ../../../bin/django-admin.py startapp relationtp

```

#### Aplicar migraciones

```sh
$ (trees_parks_rest) cd src/
$ (trees_parks_rest) python manage.py makemigrations
$ (trees_parks_rest) python manage.py migrate
```

#### Carpeta para migraciones de modelos
No olvidar archivo __init__.py
```sh
$ (trees_parks_rest) cd src/
$ (trees_parks_rest) mkdir migrations/
```

#### Iniciar
```sh
$ (rest-devcode) python manage.py runserver
```