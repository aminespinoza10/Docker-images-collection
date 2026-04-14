#!bin/bash

IMAGE_BASE_NAME="aminespinoza/website:latest"


# PASO 1: Construir la imagen de Docker y subirla a Docker Hub
cd ../React

docker build -t $IMAGE_BASE_NAME .

docker push $IMAGE_BASE_NAME

# PASO 2: Crear el recurso de AWS Elastic Beanstalk y desplegar la aplicación
# Crear un archivo Dockerrun.aws.json para Elastic Beanstalk
cat > Dockerrun.aws.json <<EOL
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "$IMAGE_BASE_NAME",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": "80"
    }
  ]
}
EOL