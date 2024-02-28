# dns_app

Simplified authoritative server for a network of applications

## Create network

``` sh
docker network create dns_app
```

## Inspect network

Docker network IP addresses:

- US (172.19.0.2)
- FS (172.19.0.3)
- AS (172.19.0.4)

This network application has IP addresses for the US, FS, and AS hardcoded in
each `run.py` file for each server respectively. These IP addresses might also
be referenced various examples in project `README.md` files. See the IP
addresses used for each of the running containers on the network using the
below command and change them throughout the codebase if necessary.

## Build

Build each image:

- [US (User server)](./US/README.md)
- [FS (Fibonacci server)](./FS/README.md)
- [AS (Authoritative server)](./AS/README.md)

## Run

Run each container:

- [US (User server)](./US/README.md)
- [FS (Fibonacci server)](./FS/README.md)
- [AS (Authoritative server)](./AS/README.md)

``` sh
docker inpect dns_app
```

## Browser

You can access the US (User server) which is considered the entry point for the
network application by using the below URL in your browser. Notice that you
access the US by referencing the IP address for localhost and not 172.19.0.2
since you're outside of the Docker network.

``` text
http://127.0.0.1:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&number=7&as_ip=172.19.0.4&as_port=53533
```
