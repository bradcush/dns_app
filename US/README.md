# User server (US)

User server (US) is a simple HTTP web server (e.g. Flask), running in port
8080, that accepts a GET HTTP requests in path:

## Build

``` sh
docker build -t dns_app/us:latest .
```

## Rum

``` sh
docker run \
    --network dns_app \
    --name dns-app-us \
    -p 8080:8080 \
    -it dns_app/us:latest
```
