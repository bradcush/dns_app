# Fibonacci server (FS)

Fibonacci Server (FS) is an HTTP web server, running in port 9090,
that provides the Fibonacci value for a given sequence number X.

## Register

`/register` accepts HTTP PUT requests that contain JSON data in the body of the
message. See the example below using `curl` for how to format a request.

``` text
curl --request PUT http://0.0.0.0:9090/register \
    --header "Content-Type: application/json" \
    --data '{"hostname":"fibonacci.com","ip": "0.0.0.0","as_ip":"0.0.0.0","as_port":"53533"}'
```
