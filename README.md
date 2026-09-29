# Proyecto Semana 7 - API Rest y Consumo de Web Service

Este repositorio contiene la entrega de la semana 7 para la asignatura de Programación Web.

## ¿Qué trae de nuevo?
- **API Propia (Categorías)**: Creé una app nueva llamada `rest_api`. Adentro están los serializadores, las urls y las vistas para compartir los datos de la tabla `Categoria` hacia el exterior.
- **Seguridad**: La API de categorías está protegida. Le configuré TokenAuthentication (DRF) para que solo usuarios autenticados puedan hacer GET, POST, PUT o DELETE.
- **Consumo de API Externa**: En el `index.html` consumimos una API pública usando `fetch` (JavaScript). Así mostramos datos externos (tarjetas de usuarios) directamente en la página principal sin tener que recargar.
- **Fixes menores**: Arreglé un detalle con el `pathlib` en los settings para que no se caiga al iniciar.

## ¿Cómo hacerlo funcionar?
1. Instalar las librerías necesarias:
   `pip install django djangorestframework cx_oracle Pillow`
2. Tener corriendo Oracle Database localmente (xe por el puerto 1521).
3. Hacer las migraciones:
   `python manage.py makemigrations`
   `python manage.py migrate`
4. Levantar el server:
   `python manage.py runserver`
   
(Para ver la API desde el navegador, entra al `/admin` con un superusuario y luego ve a `/api/categorias/`).
