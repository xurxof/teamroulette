=============
Team roulette
=============

Boostraping
-----------

1. Crear entorno virtual

   .. code::
   
       mkdir teamroulette
       cd teamroulette
       python3.4 -m venv .venv

2. Activar entorno

   Linux/Mac OS:

   .. code::

       source .venv/bin/activate

   Windows:

   .. code::

       .venv\Scripts\activate.bat

3. Instalar Django

   .. code::

       pip install django

4. Inicializar proyecto

  .. code::
  
      django-admin startproject teamroulette .

Comandos Django
---------------

.. code::

    python manage.py <comando>

Comandos:

migrate
    Aplica cambios en la base de datos

createsuperuser
    Crea un usuario administrador
    
runserver
    Lanza servidor de desarollo

shell
    Lanza un intérprete interactivo con Django configurado

startapp *<app>*
    Inicializa archivos de una aplicación Django nueva

makemigrations *<app>*
    Genera código para migración de modelos

