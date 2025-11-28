# Usamos una imagen oficial de Python
FROM python:3.10-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación
COPY app.py .

# Instalar Flask
RUN pip install flask

# Exponer el puerto donde corre la app
EXPOSE 8081

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
