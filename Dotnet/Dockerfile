FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /app
COPY Dotnet.csproj .
RUN dotnet restore
COPY . .

RUN dotnet build Dotnet.csproj -c Release -o /app/build

RUN dotnet publish Dotnet.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:9.0
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "Dotnet.dll"]