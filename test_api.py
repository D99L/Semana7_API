import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hsc.settings')
django.setup()

from django.test import Client
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from Inicio.models import Categoria

# Cleanup
User.objects.all().delete()
Categoria.objects.all().delete()

# Create user and token
user = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
token = Token.objects.create(user=user)

# Create a category
Categoria.objects.create(nombreCat='Perifericos')

# Setup client
client = Client()
headers = {'HTTP_AUTHORIZATION': f'Token {token.key}'}

# Test GET /api/categorias/
print('--- GET /api/categorias/ ---')
res = client.get('/api/categorias/', **headers)
print(res.status_code)
print(res.json())

# Test POST /api/categorias/
print('--- POST /api/categorias/ ---')
res = client.post('/api/categorias/', {'nombreCat': 'Monitores'}, content_type='application/json', **headers)
print(res.status_code)
print(res.json())

# Test Unauthorized GET
print('--- GET /api/categorias/ (Unauthorized) ---')
res_unauth = client.get('/api/categorias/')
print(res_unauth.status_code)

# Test GET detail
print('--- GET /api/categorias/2/ ---')
cat_id = res.json()["idCategoria"]
res = client.get(f'/api/categorias/{cat_id}/', **headers)
print(res.status_code)
print(res.json())

# Test PUT detail
print(f'--- PUT /api/categorias/{cat_id}/ ---')
res = client.put(f'/api/categorias/{cat_id}/', {'nombreCat': 'Monitores Actualizado'}, content_type='application/json', **headers)
print(res.status_code)
print(res.json())

# Test DELETE detail
print(f'--- DELETE /api/categorias/{cat_id}/ ---')
res = client.delete(f'/api/categorias/{cat_id}/', **headers)
print(res.status_code)

