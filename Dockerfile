# Imagen base
FROM python:3.14-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script al contenedor
COPY app.py .

# Instala Flask
RUN pip install flask

# Expone el puerto en el que correrá la app
EXPOSE 3000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]