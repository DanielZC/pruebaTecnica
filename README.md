# Solucion de prueba tecnica - Victor Daniel Zabaleta Castellar - 30/01/2023
El back end esta realizado en [Django](https://www.djangoproject.com/ "Django")

## Instalar dependencias
```
pip install -r requirements.txt
```

## Configuracion Base de datos
- Crear base de dato en postgreSQL con el nombre "productos"
- Cambiar usuario, contraseña y puerto de ser necesario en el archivo "settings.py" en la configuracion de base de datos
- Migrar tablas

```
python manage.py migrate
```

## Iniciar el servidor
```
python manage.py runserver
```