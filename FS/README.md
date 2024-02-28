# Fibonacci server (FS)

Fibonacci Server (FS) is an HTTP web server, running in port 9090,
that provides the Fibonacci value for a given sequence number X.

## Register

`/register` accepts HTTP PUT requests that contain JSON data in the body of the
message. See the example below using `curl` for how to format a request. You
may need to run this command to register a hostname with the AS.

``` sh
# Ensure correct IPs based on the network
curl --request PUT http://0.0.0.0:9090/register \
    --header "Content-Type: application/json" \
    --data '{"hostname":"fibonacci.com","ip": "172.19.0.3","as_ip":"172.19.0.4","as_port":"53533"}'
```

*Note: A file has already been created to store the DNS record specified in the
above command. If any IP addresses change you may need to rerun the above
command with those changed IP addresses to run the application.*

## Build

``` sh
docker build -t dns_app/fs:latest .
```

## Rum

``` sh
docker run \
    --network dns_app \
    --name dns-app-fs \
    -p 9090:9090 \
    -it dns_app/fs:latest
```
