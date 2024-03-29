import socket
from flask import Flask
from flask import request

app = Flask(__name__)


# Register the hostname with the
# authoritative name server over UDP
def register_hostname(hostname, ip, as_ip, as_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Format required for DNS record to be registered
    request = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10"
    sock.sendto(request.encode(), (as_ip, as_port))

    try:
        response = sock.recvfrom(2048)
        sock.close()
        print(f"Received {response}")
        # We expect to receive a success message
        return response[0].decode() == "SUCCESS"
    except socket.timeout:
        sock.close()
        print("An error occurred")
        return False


# Register a hostname and IP address
# with an authoritative DNS server
@app.route("/register", methods=["PUT"])
def register():
    body = request.get_json()
    hostname = body.get("hostname")
    ip = body.get("ip")
    as_ip = body.get("as_ip")
    as_port = body.get("as_port")

    print(hostname, ip, as_ip, as_port)
    if not (hostname) or not (ip) or not (as_ip) or not (as_port):
        return "Bad Request", 400

    # Register the hostname with the authoritative name server
    is_registered = register_hostname(hostname, ip, as_ip, int(as_port))
    if not is_registered:
        return "Internal Server Error", 500

    return "Created", 201


# Simple nth fibonacci
# number generator
def fib(n):
    first = 0
    second = 1
    for _ in range(n):
        temp = first
        first = second
        second = temp + second
    return first


# Calculate and return the nth
# fibonacci number in a sequence
@app.route("/fibonacci")
def fibonacci():
    args = request.args
    number = args.get("number")

    if not (number) or not number.isdigit():
        return "Bad Request", 400

    # 200 OK is implicit
    return str(fib(int(number)))


app.run(host="0.0.0.0", port=9090, debug=True)
