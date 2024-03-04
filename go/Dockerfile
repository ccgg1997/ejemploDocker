# Utiliza una imagen de Golang base para construir la aplicación
FROM golang:1.22.0-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código fuente de tu aplicación al directorio de trabajo del contenedor
COPY /app .

RUN chown -R 1000:1000 /app
RUN chmod -R 755 /app

# Ejecuta los comandos de compilación de Go en el Dockerfile
RUN go mod init main && \
    go mod tidy && \
    go build -o main .

# Especifica el comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["./main"]
