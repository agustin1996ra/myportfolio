# Usar una imagen base de Python
FROM python:3.11.4-bookworm

# Directorio de trabajo
WORKDIR /app

# Archivos requisitos
COPY requirements.txt /app/

# Instalacion de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el codigo de la aplicacion
COPY . /app/

# Exponer el puerto que utiliza la aplicacion
EXPOSE 8000

# Comando para la ejecucion de la aplicacion
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 
