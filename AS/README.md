# Authoritative server (AS)

Authoritative Server (AS) is the authoritative server for US. It has two
duties. First is to handle the registration requests to pair hostnames to IP,
second is to be able to respond to DNS queries from clients.

## Build

``` sh
docker build -t dns_app/as:latest .
```

## Rum

``` sh
docker run \
    --network dns_app \
    --name dns-app-as \
    -p 53533:53533/udp \
    -it dns_app/as:latest
```
