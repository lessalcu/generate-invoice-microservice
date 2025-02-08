FROM python:3.9

WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Definir la variable de entorno para Flask
ENV FLASK_APP=app.py

# Exponer el puerto
EXPOSE 5005

# Comando para ejecutar la aplicación
CMD ["python", "/app/app.py"]
