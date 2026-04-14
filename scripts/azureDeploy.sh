#!bin/bash

SERVICE_NAME="aminwebsite"
RESOURCE_GROUP="LiveAmin"
LOCATION="East US 2"
CONTAINER_APP_ENV="aminespinoza"
IMAGE_BASE_NAME="aminespinoza/website:latest"

# PASO 1: Construir la imagen de Docker y subirla a Docker Hub
cd ../React

docker build -t $IMAGE_BASE_NAME .

docker push $IMAGE_BASE_NAME

# PASO 2: Crear el recurso de Azure Container Apps y desplegar la aplicación

#ejecución de una sola vez para instalar la extensión de containerapp
az config set extension.use_dynamic_install=yes_without_prompt

az resource group create --name $RESOURCE_GROUP --location $LOCATION

az containerapp env create --name $CONTAINER_APP_ENV --resource-group $RESOURCE_GROUP --location $LOCATION

az containerapp up --name "$SERVICE_NAME" --resource-group $RESOURCE_GROUP --environment $CONTAINER_APP_ENV --image $IMAGE_BASE_NAME --target-port 80 --ingress external