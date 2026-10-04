import os

path = 'semana 8/Hsc/Inicio/templates'
replacements = {
    'Acǭ podrǭs': 'Acá podrás',
    'PerifǸricos': 'Periféricos',
    'MICR"FONOS': 'MICRÓFONOS',
    'MICRÃ“FONOS': 'MICRÓFONOS',
    'TARJETAS GR?FICAS': 'TARJETAS GRÁFICAS',
    'TARJETAS GRÃ FICAS': 'TARJETAS GRÁFICAS',
    'InformaciÃ³n': 'Información',
    'Informacin': 'Información',
    'pǧblico': 'público',
    'pÃºblico': 'público',
    'AÃ±adir': 'Añadir',
    'CatÃ¡logo': 'Catálogo',
    'RegiÃ³n': 'Región',
    'ContraseÃ±a': 'Contraseña'
}

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
            
            for bad, good in replacements.items():
                content = content.replace(bad, good)
            
            # Additional fixes based on regex or byte fixing could be done
            content = content.replace('Ã¡', 'á').replace('Ã©', 'é').replace('Ã­', 'í').replace('Ã³', 'ó').replace('Ãº', 'ú').replace('Ã±', 'ñ')
            content = content.replace('Ã', 'Á').replace('Ã‰', 'É').replace('Ã', 'Í').replace('Ã“', 'Ó').replace('Ãš', 'Ú').replace('Ã‘', 'Ñ')
            content = content.replace('Â¿', '¿').replace('Â¡', '¡')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
print('Templates reparados.')