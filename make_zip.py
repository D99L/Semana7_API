import os
import zipfile

def create_zip(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Excluir carpetas innecesarias o pesadas
            dirs[:] = [d for d in dirs if d not in ['venv', '__pycache__']]
            for file in files:
                if file.endswith('.pyc'):
                    continue
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

create_zip(r'C:\Users\Adolfo\Desktop\programacion web\semana 7\Hsc', r'C:\Users\Adolfo\Desktop\Entrega_Semana7_Proyecto.zip')
